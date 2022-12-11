from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers


class UniteApiViewSet(viewsets.ModelViewSet):

    queryset = models.Unite.objects.order_by('id')
    serializer_class = serializers.UniteSerializer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'category',


class CategoryApiViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.order_by('id')
    serializer_class = serializers.CategorySerializer
    permission_classes = permissions.IsAuthenticated,


class SubCategoryApiViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategory.objects.order_by('id')
    serializer_class = serializers.SubCategorySerializer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend,
    filterset_fields = 'category',
