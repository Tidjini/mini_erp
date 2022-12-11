from rest_framework import serializers

from . import models


class UniteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Unite
        fields = '__all__'
        read_only_fields = 'id',
        