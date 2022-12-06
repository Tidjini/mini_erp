from django.db import models

from .product import Product
from apps.application import fileds


class DetailReception(models.Model):

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='receptions')
    qte = fileds.AppDecimalField()
    prix_unite = fileds.AppDecimalField()
