from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from . import models, serializers


# done for list, get created tasks for creator
# done for list, get tasks for receiver
# todo set finish request in separete view set with function based
class TaskApiViewSet(viewsets.ModelViewSet):

    queryset = models.Task.objects.order_by('-created_at')
    serializer_class = serializers.TaskSerialzer
    permission_classes = permissions.IsAuthenticated,

    def list(self, request, *args, **kwargs):

        user = request.user
        if not user:
            return Response({'detail': 'you must specify the task user (creator or receiver), put token in the header'}, status=status.HTTP_401_UNAUTHORIZED)
        # type get params: to specify the request user, is he wants get created ones or received ones
        type = request.query_params.get('type', None)
        if type is None:
            return Response({'detail': 'you must specify the user type (creator or receiver), in request get params'}, status=status.HTTP_401_UNAUTHORIZED)

        if type == "0":
            self.queryset = models.Task.objects.filter(
                creator=user.id)
        else:
            self.queryset = models.Task.objects.filter(receiver=user.id)

        self.queryset = self.queryset.order_by('-created_at')

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        creator = request.user
        if not creator:
            return Response({'detail': 'you must specify the task creator, put token in the header'}, status=status.HTTP_401_UNAUTHORIZED)
        request.data.update({'creator': request.user.id})

        return super().create(request, *args, **kwargs)
