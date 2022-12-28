from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.communications.views import sio
from . import models
from .notification import NotificationAPI

# @receiver(post_save, sender=models.Task)
# def notify_users(sender, instance, created, **kwargs):

#     if not created:
#         event = f'{instance.creator.token_key}_tasks'
#         sio.emit(event, instance.label)

#     if instance.receiver:
#         event = f'{instance.receiver.token_key}_tasks'
#         sio.emit(event, instance.label)


@receiver(post_save, sender=models.Task)
def notify_users(sender, instance, created, **kwargs):

    data = {key: val for key, val in instance.__dict__.items() if key in (
            'id', 'label', 'description')}

    print('created', created)
    if instance.statue == 'i' and instance.receiver:
        token = instance.receiver.token_key
        NotificationAPI.send(None, 'tasks', token, data)
        return

    if instance.creator:
        token = instance.creator.token_key
        NotificationAPI.send(None, 'tasks', token, data)
