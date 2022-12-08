from rest_framework import viewsets, permissions

from . import models, serializers


# todo for list, get created tasks for creator
# todo for list, get tasks for receiver
class TaskApiViewSet(viewsets.ModelViewSet):

    queryset = models.Task.objects.order_by('-created_at')
    serializer_class = serializers.TaskSerialzer
    permission_classes = permissions.IsAuthenticated

