from django.db.models.signals import post_save
from django.dispatch import receiver

from . import models
from apps.communications.views import sio


@receiver(post_save, sender=models.Payment)
def update_balance(sender, instance, created, **kwargs):

    if not instance.third:
        return

    if instance.out:
        instance.third.credit += instance.amount
    else:
        instance.third.debit += instance.amount

    instance.third.save()

    sio.emit('payment_added', instance.label)
