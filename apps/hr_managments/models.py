from django.db import models
from apps.application.models import UtilsMixin
from apps.general.models import Profile


class Employe(UtilsMixin):

    TYPES = (
        ('C', 'CHAUFFEUR'),
        ('A', 'ADMINISTRATION'),
        ('O', 'OTHER'),
    )
    user = models.OneToOneField(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=2, choices=TYPES, default='O')


class Localisation(UtilsMixin):

    user = models.OneToOneField(
        Profile, primary_key=True, on_delete=models.CASCADE)
    longitude = models.DecimalField(
        max_digits=50, decimal_places=20, default=0)
    latitude = models.DecimalField(max_digits=50, decimal_places=20, default=0)
