from django.db import models
from apps.general.models import Profile


class Task(models.Model):

    STATUES = (
        ('i', 'instance'),
        ('a', 'accepted'),
        ('t', 'terminated'),
        ('c', 'canceled')
    )
    creator = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='created_tasks')
    receiver = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True,
        related_name='tasks')

    statue = models.CharField(max_length=1, choices=STATUES, default='i')

    label = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
