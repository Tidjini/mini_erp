from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from . import models


@receiver(pre_save, sender=models.StockMovement)
def remove_stock(sender, instance, **kwargs):

    if instance.pk:
        # when updating remove old stock from this one, if out must readd the entity, else remove it
        try:
            old = models.StockMovement.objects.get(id=instance.pk)
            sign = 1
            if old.out:
                sign = -1

            instance.product.stock_qte -= old.qte * sign
            # update value just for receptions
            instance.product.stock_value -= old.qte * sign * old.value

            instance.product.save()
        except Exception as e:
            pass


@receiver(post_save, sender=models.StockMovement)
def add_stock(sender, instance, created, **kwargs):
    # if stock out remove qte, else add this reception
    sign = 1
    if instance.out:
        sign = -1
    instance.product.stock_qte += instance.qte * sign

    # update value just for receptions
    instance.product.stock_value += instance.qte * sign * instance.value

    if instance.product.stock_qte < 0:
        instance.product.stock_qte = 0
    if instance.product.stock_value < 0:
        instance.product.stock_value = 0
    instance.product.save()
