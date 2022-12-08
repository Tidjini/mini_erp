from rest_framework import viewsets, permissions

from . import models
from . import serializers


class ProductApiViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.order_by('-id')
    serializer_class = serializers.ProductSerializer
    permission_classes = permissions.IsAuthenticated,


class StockMovementApiViewSet(viewsets.ModelViewSet):
    queryset = models.StockMovement.objects.order_by('-created_at')
    serializer_class = serializers.StockMovementSerializer
    permission_classes = permissions.IsAuthenticated,


class TierApiViewSet(viewsets.ModelViewSet):
    queryset = models.Tier.objects.order_by('-id')
    serializer_class = serializers.TierSerializer
    permission_classes = permissions.IsAuthenticated,


class PaymentApiViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.order_by('-created_at')
    serializer_class = serializers.PaymentSerializer
    permission_classes = permissions.IsAuthenticated,
