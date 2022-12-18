from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from apps.application.response import auth_response
from . import serializers, models


class TvaApiViewSet(viewsets.ModelViewSet):

    queryset = models.Tva.objects.all()
    serializer_class = serializers.TvaSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None


class ProfileListApiViewSet(viewsets.ModelViewSet):

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = permissions.AllowAny,
    filter_backends = filters.OrderingFilter,
    ordering_fields = 'name', 'telephone', 'exercice'
    pagination_class = None

    def create(self, request, *args, **kwargs):
        # override create to send token to user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        # set token with user (profile) data
        response = auth_response(instance, serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(response, status=status.HTTP_201_CREATED, headers=headers)


class AuthenticationAPI:

    @staticmethod
    def response(user, *args, **kwargs):
        serializer = serializers.ProfileSerializer(user)
        response = auth_response(user, serializer)
        return Response(response, status=status.HTTP_200_OK)

    @api_view(('GET',))
    @permission_classes((permissions.IsAuthenticated,))
    @staticmethod
    def token(request, *args, **kwargs):
        # set request header with Authorisation: token xxxxxxxxxxxxxx
        user = request.user
        return AuthenticationAPI.response(user)

    @api_view(('POST', ))
    @staticmethod
    def username(request, *args, **kwargs):
        uname = request.data.get('username')
        pwd = request.data.get('password')
        user = models.ProfileAPI.username_auth(uname, pwd)
        if user:
            return AuthenticationAPI.response(user)
        return Response('User not exist', status=status.HTTP_404_NOT_FOUND)
