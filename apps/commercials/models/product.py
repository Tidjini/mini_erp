from django.db import models

from apps.application import fileds
from datetime import datetime


class Product(models.Model):

    name = models.CharField(max_length=255)
    qte_stock = fileds.AppDecimalField(default=0.0)
    pre_qte_stock = fileds.AppDecimalField(default=0.0)
    value = fileds.AppDecimalField(default=0.0)
    pre_value = fileds.AppDecimalField(default=0.0)

    unite = models.CharField(max_length=10, default='unite')

    # todo review the delete process, not delete or delete with conditions


class StockMovement(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='movements')
    qte = fileds.AppDecimalField()
    prix_unite = fileds.AppDecimalField()
    out = models.BooleanField()
    document = models.CharField(max_length=255)

    date_creation = models.DateTimeField(auto_now_add=True)
