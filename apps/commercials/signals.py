from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


from . import models

# todo later
# @receiver(pre_save, sender=models.DetailReception)
# def remove_stock(sender, instance, **kwargs):

#     if instance.pk:
#         # when updating remove old stock from this one
#         try:
#             old = models.DetailReception.objects.get(id=instance.pk)
#             instance.product.qte_stock -= old.qte
#             instance.product.save()
#         except Exception as e:
#             pass


# @receiver(post_save, sender=models.DetailReception,)
# def add_stock(sender, instance, created, **kwargs):
#     instance.product.qte_stock += instance.qte
#     instance.product.save()


@receiver(pre_save, sender=models.StockMovement)
def remove_stock(sender, instance, **kwargs):

    if instance.pk:
        # when updating remove old stock from this one, if out must readd the entity, else remove it
        try:
            old = models.DetailReception.objects.get(id=instance.pk)
            sign = 1
            if old.out:
                sign = -1

            instance.product.qte_stock -= old.qte * sign
            instance.product.save()
        except Exception as e:
            pass


@receiver(post_save, sender=models.StockMovement)
def add_stock(sender, instance, created, **kwargs):
    # if stock out remove qte, else add this reception
    sign = 1
    if instance.out:
        sign = -1
    instance.product.qte_stock += instance.qte * sign
    instance.product.save()
