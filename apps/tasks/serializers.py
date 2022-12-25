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

    locations = TaskLocationSerializer(
        source='path', read_only=True, many=True)
    documents = TaskAttachementSerializer(
        source='task_docs', read_only=True, many=True)

    caption = serializers.ReadOnlyField()
    statue_label = serializers.ReadOnlyField()
    closed = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    created_time = serializers.ReadOnlyField()
    receiver_name = serializers.ReadOnlyField()
    creator_name = serializers.ReadOnlyField()
    has_location = serializers.ReadOnlyField()

    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = 'id',


class TaskLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TaskLocation
        fields = '__all__',
        read_only_fields = 'id',
