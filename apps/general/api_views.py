from rest_framework import viewsets, permissions, filters, status, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from apps.application.response import auth_response
from . import serializers, models


class TvaApiViewSet(viewsets.ModelViewSet):

    queryset = models.Tva.objects.all()
    serializer_class = serializers.TvaSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None


class LocalisationApi(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = models.Localisation.objects.all()
    serializer_class = serializers.LocalisationSerializer
    permission_classes = permissions.IsAuthenticated,
    pagination_class = None

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        print('in create', request.user.name)

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.user = request.user.id
        request.data['user'] = request.user.id
        print('in update', request.user.name)
        try:
            return super(LocalisationApi, self).update(request, *args, **kwargs)
        except:
            return super().create(request, *args, **kwargs)


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


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def update_profile_state(request):

    user = request.user
    if not user.is_admin and not user.is_staff:
        return Response({'Details': 'User must be a staff or administrator to patch the user profile state'}, status=status.HTTP_401_UNAUTHORIZED)

    data = request.data
    try:
        profile = models.Profile.objects.get(pk=data['pk'])
        profile.statue = data['statue']
        profile.save_base()
    except models.Profile.DoesNotExist:
        return Response({'Details': 'Profile does not exist'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'data': request.data}, status=status.HTTP_200_OK)


class AuthenticationAPI:

    # @staticmethod
    def response(user, *args, **kwargs):
        serializer = serializers.ProfileSerializer(user)
        response = auth_response(user, serializer)
        return Response(response, status=status.HTTP_200_OK)

    @api_view(('GET',))
    @permission_classes((permissions.IsAuthenticated,))
    # @staticmethod
    def token(request, *args, **kwargs):
        # set request header with Authorisation: token xxxxxxxxxxxxxx
        user = request.user
        return AuthenticationAPI.response(user)

    @api_view(('POST', ))
    # @staticmethod
    def username(request, *args, **kwargs):
        uname = request.data.get('username')
        pwd = request.data.get('password')
        user = models.ProfileAPI.username_auth(uname, pwd)
        if user:
            return AuthenticationAPI.response(user)
        return Response('User not exist', status=status.HTTP_404_NOT_FOUND)
