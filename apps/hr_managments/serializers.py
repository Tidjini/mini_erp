from rest_framework import serializers

from apps.general.serializers import ProfileSerializer
from . import models


class EmployeSerializer(serializers.ModelSerializer):

    user = ProfileSerializer(source='profile', read_only=True)

    class Meta:
        model = models.Employe
        fields = '__all__'
        read_only_fields = 'id',
