from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from apps.general.models import ProfileAPI
from apps.application.response import auth_response
from .. import serializers


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
        print(f'user: {uname}, {pwd}')
        user = ProfileAPI.username_auth(uname, pwd)
        if user:
            return AuthenticationAPI.response(user)
        return Response('User not exist', status=status.HTTP_404_NOT_FOUND)
