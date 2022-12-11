from django.db import models


class Tva(models.Model):
    tva = models.CharField(max_length=50, unique=True)
    value = models.DecimalField(
        decimal_places=3, max_digits=5, default=0.19)
