from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.general import api_views as general
from apps.chats import api_views as chats
# from apps.commercials import api_views as commercials
from apps.accountings import api_views as accounts
from apps.tasks import api_views as tasks
from apps.stock import api_views as stock

router = DefaultRouter()

# general
router.register('tvas', general.TvaApiViewSet)

# chats
router.register('utilisateurs', chats.UtilisateurListApiViewSet)
router.register('discussions', chats.DiscussionApiViewSet)
router.register('messages', chats.MessageApiViewSet)
# commecrials
router.register('thirds', accounts.ThirdApiViewSet)
router.register('payments', accounts.PaymentApiViewSet)
# tasks
router.register('tasks', tasks.TaskApiViewSet)
# stocks
router.register('unites', stock.UniteApiViewSet)
router.register('categories', stock.CategoryApiViewSet)
router.register('sub-categories', stock.SubCategoryApiViewSet)
router.register('products', stock.ProductApiViewSet)
router.register('stock-movements', stock.StockMovementApiViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/token/', chats.AuthenticationAPI.token,
         name='Token Authentication'),
    path('api/auth/username/', chats.AuthenticationAPI.username,
         name='Username Authentication')
]
