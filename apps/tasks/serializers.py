from rest_framework import serializers

from . import models
from apps.general.serializers import ProfileSerializer


class TaskSerialzer(serializers.ModelSerializer):

    receiver_item = ProfileSerializer(source='receiver', read_only=True)
    caption = serializers.ReadOnlyField()
    statue_label = serializers.ReadOnlyField()

    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = 'id',
