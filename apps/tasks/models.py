from django.db import models
from apps.chats.models import Utilisateur
from apps.application.models import UtilsMixin


class Task(models.Model):

    STATUES = (
        ('i', 'instance'),
        ('a', 'accepted'),
        ('t', 'terminated'),
        ('c', 'canceled')
    )
    creator = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='created_tasks')
    receiver = models.ForeignKey(
        Utilisateur, on_delete=models.SET_NULL, null=True,
        related_name='tasks')

    statue = models.CharField(max_length=1, choices=STATUES, default='i')

    label = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Localisation(UtilsMixin):
    user = models.OneToOneField(Utilisateur, primary_key=True)
    latitude = models.DecimalField(max_digits=50, decimal_places=20, default=0)
    longitude = models.DecimalField(
        max_digits=50, decimal_places=20, default=0)
