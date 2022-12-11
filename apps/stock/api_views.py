from rest_framework import viewsets, permissions

from . import models, serializers


class UniteApiViewSet(viewsets.ModelViewSet):

    queryset = models.Unite.objects.all()
    serializer_class = serializers.UniteSerializer
    permission_classes = permissions.IsAuthenticated,
