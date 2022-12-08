from rest_framework import serializers

from . import models
from apps.chats.serializers import UtilisateurSerializer


class TaskSerialzer(serializers.ModelSerializer):

    receiver_item = UtilisateurSerializer(source='receiver', read_only=True)

    class Meta:
        model = models.Task
        fields = '__all__'
        read_only_fields = 'id',
