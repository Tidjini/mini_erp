from django.db import models
from apps.application import fileds


class Tier(models.Model):
    TYPES = (
        ('c', 'client'),
        ('p', 'provider'), 
        ('f', 'fabricant'),
        ('t', 'tier'),
    )
    
    # raison social
    label = models.CharField(max_length=255)
    debit = fileds.AppDecimalField()
    credit = fileds.AppDecimalField()
    type = models.CharField(max_length=1, choices=TYPES ,default='t')

    @property
    def balance(self):
        return self.debit - self.credit


class Payment(models.Model):
    tier = 