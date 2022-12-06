from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.chats import api_views as chats
from apps.commercials import api_views as commercials

router = DefaultRouter()
# chats
router.register('utilisateurs', chats.UtilisateurListApiViewSet)
router.register('discussions', chats.DiscussionApiViewSet)
router.register('messages', chats.MessageApiViewSet)
# commecrials
router.register('products', commercials.ProductApiViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/token/', chats.AuthenticationAPI.token,
         name='Token Authentication'),
    path('api/auth/username/', chats.AuthenticationAPI.username,
         name='Username Authentication')
]
