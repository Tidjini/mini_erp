from django.db import models

# application
from apps.application import models as app_models


class Unite(app_models.UtilsMixin):

    unite = models.CharField(max_length=15)
    symbole = models.CharField(max_length=15)
    coefficient = models.DecimalField(
        decimal_places=3, max_digits=8, default=1)
    # represent unite family, volume, surface, linear, ... Galenic
    # must introduce a list
    category = models.CharField(max_length=50, default='galenic')


class Category(app_models.UtilsMixin):
    name = models.CharField(max_length=50)


class SubCategory(app_models.UtilsMixin):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(max_length=50)
