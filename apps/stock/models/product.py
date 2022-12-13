from django.db import models

from apps.application import models as app_models, fileds as app_fields
from .base import Unite, Category, SubCategory
from apps.general.models import Tva
from apps.accountings.models import Third
from apps.stock.managers import ProductQuerySet


# TODO review consomable terme, and if we can separete the Services into other Table
class Product(app_models.UtilsMixin):

    TYPES = (
        ('P', 'Product'),
        ('RM', 'Raw Material'),
        ('FP', 'Final product'),
        ('SFP', 'Semi Finished product'),
        ('S', 'Service')
    )

    name = models.CharField(max_length=255)
    reference = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.SET_NULL, null=True)

    type = models.CharField(max_length=3, choices=TYPES, default='P')
    unite = models.ForeignKey(Unite, on_delete=models.SET_NULL, null=True)

    stock_qte = app_fields.DecimalField()
    # to convert between unites
    unite_coef = app_fields.DecimalField()
    # todo define process - FIFO - LIFO - CUMP
    unite_value = app_fields.DecimalField()
    stock_value = app_fields.DecimalField()

    # qté d'approvisionnement to notify
    supply_qte = app_fields.DecimalField()
    # minimum qté
    min_qte = app_fields.DecimalField()

    tva = models.ForeignKey(Tva, on_delete=models.SET_NULL, null=True)
    # fournisseur
    provider = models.ForeignKey(
        Third, on_delete=models.SET_NULL, null=True, related_name='provides')
    # fabricant
    maker = models.ForeignKey(
        Third, on_delete=models.SET_NULL, null=True, related_name='products')
    # notification to not purchase within this period (period in days)
    purchase_period = models.IntegerField(default=30)
    # purchase rate, compare to last (Todo or maybe the max) purchase
    purchase_rate = models.FloatField(default=5)

    # to track latest updated, order
    updated_at = models.DateTimeField(auto_now_add=True)
    # custom manager
    objects = ProductQuerySet.as_manager()

    class Meta:
        ordering = '-updated_at',


class Composition(app_models.UtilsMixin):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='composed_by')
    qte = app_fields.DecimalField()
    composer = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name='composed_in')


# last purchase informations
# last buy informations
# DONE filtering : Products, Services, ....
# filtering : Category, Sub Category


class StockMovement(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='sock_movements')
    qte = app_fields.DecimalField()
    value = app_fields.DecimalField()
    out = models.BooleanField(default=False)
    document = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
