from django.db import models
from apps.application import fileds


# todo set specific collections; Tiers, Providers, Fabricants, Clients

class Third(models.Model):
    TYPES = (
        ("c", "client"),
        ("p", "provider"),
        ("f", "fabricant"),
        ("t", "third"),
    )

    # raison social
    label = models.CharField(max_length=255)
    debit = fileds.AppDecimalField()
    credit = fileds.AppDecimalField()
    type = models.CharField(max_length=1, choices=TYPES, default="t")

    @property
    def balance(self):
        return self.debit - self.credit


# todo set specific collections; Payements Tiers,Payements Providers, Payements Fabricants,Payements Clients
class Payment(models.Model):
    third = models.ForeignKey(
        Third, on_delete=models.CASCADE, related_name="payments")
    label = models.CharField(max_length=255)
    amount = fileds.AppDecimalField()
    out = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
