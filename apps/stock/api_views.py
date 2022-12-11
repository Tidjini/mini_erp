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
