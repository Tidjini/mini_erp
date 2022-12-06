from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from . import models


@receiver(pre_save, sender=models.DetailReception)
def remove_stock(sender, instance, **kwargs):

    if instance.pk:
        # when updating remove old stock from this one
        try:
            old = models.DetailReception.objects.get(id=instance.pk)
            instance.product.qte_stock -= old.qte
            instance.product.save()
        except Exception as e:
            pass


@receiver(post_save, sender=models.DetailReception,)
def add_stock(sender, instance, created, **kwargs):
    instance.product.qte_stock += instance.qte
    instance.product.save()
