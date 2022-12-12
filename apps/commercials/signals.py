

from . import models, serializers
from apps.communications.views import sio


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
