from rest_framework import serializers

from . import models


class TvaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tva
        fields = '__all__'
        read_only_fields = 'id',
