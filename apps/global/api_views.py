from rest_framework import viewsets, permissions


from . import serializers, models


class TvaApiViewSet(viewsets.ModelViewSet):

    queryset = models.Tva.objects.all()
    serializer_class = serializers.TvaSerializer
    permission_classes = permissions.IsAuthenticated
    pagination_class = None
