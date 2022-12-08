from django.db import models
from apps.application import fileds


class Tier(models.Model):

    # raison social
    label = models.CharField(max_length=255)
    debit = fileds.AppDecimalField()
    credit = fileds.AppDecimalField()

    @property
    def balance(self):
        return self.debit - self.credit
