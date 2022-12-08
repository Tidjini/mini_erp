from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.communications.views import sio
from . import models


@receiver(post_save, sender=models.Task)
def notify_users(sender, instance, created, **kwargs):

    if not created:
        event = f'{instance.creator.token_key}_tasks'
        sio.emit(event, instance.label)

    if instance.receiver:
        event = f'{instance.receiver.token_key}_tasks'
        sio.emit(event, instance.label)
