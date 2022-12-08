from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from . import models, serializers


# todo for list, get created tasks for creator
# todo for list, get tasks for receiver
class TaskApiViewSet(viewsets.ModelViewSet):

    queryset = models.Task.objects.order_by('-created_at')
    serializer_class = serializers.TaskSerialzer
    permission_classes = permissions.IsAuthenticated,

    def create(self, request, *args, **kwargs):

        creator = request.user
        if not creator:
            return RecursionError
        request.data.update({'creator': request.user.id})

        return super().create(request, *args, **kwargs)
