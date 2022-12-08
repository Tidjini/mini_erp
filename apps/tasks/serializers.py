from rest_framework import serializers

from . import models

class TaskSerialzer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = 'id',