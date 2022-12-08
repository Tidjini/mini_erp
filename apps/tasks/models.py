from django.db import models
from apps.chats.models import Utilisateur


class Task(models.Model):

    STATUES = (
        ('i', 'instance'),
        ('a', 'accepted'),
        ('t', 'terminated'),
        ('c', 'canceled')
    )
    creator = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='created_tasks')
    receiver = models.ForeignKey(
        Utilisateur, on_delete=models.SET_NULL, null=True, 
        related_name='tasks')

    statue = models.CharField(max_length=1, choices=STATUES, default='i')

    label = models.CharField(max_length=255)
    description = models.TextField()
    


