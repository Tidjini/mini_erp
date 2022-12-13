from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from . import models


def clean_negative_value(product):
    if product.stock_qte < 0:
        product.stock_qte = 0
    if product.stock_value < 0:
        product.stock_value = 0


def update_product(product, qte, value, reverse=1):

    actuel_qte = qte * reverse
    actuel_value = value * reverse

    product.stock_qte += actuel_qte
    product.stock_value += actuel_value
    clean_negative_value(product)

    # update compositions
    for composition in product.compositions.all():
        prod = composition.product
        prod.stock_qte = actuel_qte * composition.qte
        prod.stock_qte = actuel_value * composition.qte
        clean_negative_value(prod)
        prod.save()

    product.save()


@receiver(pre_save, sender=models.StockMovement)
def remove_stock(sender, instance, **kwargs):

    if instance.pk:
        # when updating remove old stock from this one, if out must readd the entity, else remove it
        try:
            old = models.StockMovement.objects.get(id=instance.pk)
            sign = 1
            if old.out:
                sign = -1

            qte = old.qte * sign
            # update value just for receptions
            value = old.qte * sign * old.value
            # -1 to inverse
            update_product(instance.product, qte, value, reverse=-1)
        except Exception as e:
            pass


@receiver(post_save, sender=models.StockMovement)
def add_stock(sender, instance, created, **kwargs):
    # if stock out remove qte, else add this reception
    sign = 1
    if instance.out:
        sign = -1
    qte = instance.qte * sign
    value = instance.qte * sign * instance.value
    update_product(instance.product, qte, value)
