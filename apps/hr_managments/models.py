from django.db import models
from apps.application.models import UtilsMixin
from apps.general.models import Profile


class Employe(UtilsMixin):
    # simple Employe Table, with fixed Employe Types
    # linked to user table, wich can be null for none users
    TYPES = (
        ('D', 'DRIVER'),
        ('A', 'ADMINISTRATION'),
        ('O', 'OTHER'),
    )
    user = models.OneToOneField(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=2, choices=TYPES, default='O')


class Localisation(UtilsMixin):

    # track users by GPS provider (Android Service or other)
    # lat, lng for localisation
    # todo later add more infromation, region, zone ...
    user = models.OneToOneField(
        Profile, primary_key=True, on_delete=models.CASCADE)
    longitude = models.DecimalField(
        max_digits=50, decimal_places=20, default=0)
    latitude = models.DecimalField(max_digits=50, decimal_places=20, default=0)
