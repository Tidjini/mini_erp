from rest_framework import viewsets, permissions, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializers


# done for list, get created tasks for creator
# done for list, get tasks for receiver
# todo set finish request in separete view set with function based
# todo set Page Response with number of pages, and current page ex : 10/100
class TaskApiViewSet(viewsets.ModelViewSet):

    queryset = models.Task.objects.order_by('-created_at')
    serializer_class = serializers.TaskSerialzer
    permission_classes = permissions.IsAuthenticated,
    filter_backends = DjangoFilterBackend, filters.SearchFilter
    search_fields = 'label', 'description'

    filterset_fields = {
        "created_at": ('date',),
        "statue": ('exact',),
        "creator": ('exact',),
        "receiver": ('exact',)
    }

    def list(self, request, *args, **kwargs):

        user = request.user
        if not user:
            return Response({'detail': 'you must specify the task user (creator or receiver), put token in the header'}, status=status.HTTP_401_UNAUTHORIZED)
        # type get params: to specify the request user, is he wants get created ones or received ones
        type = request.query_params.get('type', None)
        closed = request.query_params.get('closed', None)

        # if type is None:
        #     return Response({'detail': 'you must specify the user type (creator or receiver), in request get params'}, status=status.HTTP_404_NOT_FOUND)

        if user.is_admin or user.is_staff:
            self.queryset = self.queryset.state(
                closed).order_by('-created_at')
        else:
            self.queryset = self.queryset.user_tasks(user, type).state(
                closed).order_by('-created_at')

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):

        creator = request.user
        if not creator:
            return Response({'detail': 'you must specify the task creator, put token in the header'}, status=status.HTTP_401_UNAUTHORIZED)
        request.data.update({'creator': request.user.id})

        return super().create(request, *args, **kwargs)


class TaskLocationApiView(viewsets.ModelViewSet):
    queryset = models.TaskLocation.objects.order_by('id')
    serializer_class = serializers.TaskLocationSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None

    def get_of_today(self):
        self.queryset = self.queryset.today()

    def get_by_task(self, task):
        self.queryset = self.queryset.location_task(task)

    def list(self, request, *args, **kwargs):

        task = request.query_params.get('task', None)

        if task is None and (request.user.is_admin or request.user.is_staff):
            self.get_of_today()
        elif task.isdigit():
            task = int(task)
            self.get_by_task(task)
        else:
            return Response({'detail': 'you must specify the task, {params: task<id:int>}'}, status=status.HTTP_404_NOT_FOUND)

        return super().list(request, *args, **kwargs)
