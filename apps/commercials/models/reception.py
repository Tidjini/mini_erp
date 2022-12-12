from django.db import models

from apps.stock import models as stock
from apps.application import fileds


class DetailReception(models.Model):

    product = models.ForeignKey(
        stock.Product, on_delete=models.CASCADE, related_name='receptions')
    qte = fileds.AppDecimalField()
    prix_unite = fileds.AppDecimalField()
