from rest_framework import viewsets, permissions

from . import models
from . import serializers


class ThirdApiViewSet(viewsets.ModelViewSet):
    queryset = models.Third.objects.order_by('-id')
    serializer_class = serializers.ThirdSerializer
    permission_classes = permissions.IsAuthenticated,


class PaymentApiViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.order_by('-created_at')
    serializer_class = serializers.PaymentSerializer
    permission_classes = permissions.IsAuthenticated,
