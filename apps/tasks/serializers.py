from rest_framework import serializers

from . import models
from apps.general.serializers import ProfileSerializer


class TaskLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TaskLocation
        fields = '__all__'
        read_only_fields = 'task',


class TaskAttachementSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TaskAttachement
        fields = '__all__'
        read_only_fields = 'task',


class TaskSerialzer(serializers.ModelSerializer):

    receiver_item = ProfileSerializer(source='receiver', read_only=True)
    locations = TaskLocationSerializer(
        source='path', read_only=True, many=True)
    documents = TaskAttachementSerializer(
        source='task_docs', read_only=True, many=True)

    caption = serializers.ReadOnlyField()
    statue_label = serializers.ReadOnlyField()

    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = 'id',
