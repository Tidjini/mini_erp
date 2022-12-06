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
    out = models.BooleanField(default=False)
    document = models.CharField(max_length=255)

    date_creation = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     # if stock out remove qte, else add this reception
    #     sign = 1
    #     if self.out:
    #         sign = -1
    #     self.product.qte_stock += self.qte * sign
    #     self.product.value += self.qte * sign * self.prix_unite
    #     self.product.save()
    #     return super(StockMovement, self).save(*args, **kwargs)
