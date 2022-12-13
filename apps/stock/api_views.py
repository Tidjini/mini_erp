from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers


class UniteApiViewSet(viewsets.ModelViewSet):

    queryset = models.Unite.objects.all()
    serializer_class = serializers.UniteSerializer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'category',
    pagination_class = None


class CategoryApiViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None


class SubCategoryApiViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'category',
    pagination_class = None


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'category', 'sub_category', 'provider', 'maker', 'type'


class StockMovementApiViewSet(viewsets.ModelViewSet):
    queryset = models.StockMovement.objects.order_by('-created_at')
    serializer_class = serializers.StockMovementSerializer
    permission_classes = permissions.IsAuthenticated,


class CompositionApiViewSet(viewsets.ModelViewSet):
    queryset = models.Composition.objects.order_by('-id')
    serializer_class = serializers.CompositionSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None
