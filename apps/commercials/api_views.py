from rest_framework import viewsets, permissions

from . import models
from . import serializers


class ProductApiViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = permissions.IsAuthenticated,
