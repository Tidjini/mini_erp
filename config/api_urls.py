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
router.register('profiles', general.ProfileListApiViewSet)
router.register('localisations', general.LocalisationApi)

# chats
router.register('discussions', chats.DiscussionApiViewSet)
router.register('messages', chats.MessageApiViewSet)
# commecrials
router.register('thirds', accounts.ThirdApiViewSet)
router.register('payments', accounts.PaymentApiViewSet)
# tasks
router.register('tasks', tasks.TaskApiViewSet)
router.register('task-localisations', tasks.TaskLocationApiView)
# stocks
router.register('unites', stock.UniteApiViewSet)
router.register('categories', stock.CategoryApiViewSet)
router.register('sub-categories', stock.SubCategoryApiViewSet)
router.register('products', stock.ProductApiViewSet)
router.register('stock-movements', stock.StockMovementApiViewSet)
router.register('compositions', stock.CompositionApiViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/token/', general.AuthenticationAPI.token,
         name='Token Authentication'),
    path('api/auth/username/', general.AuthenticationAPI.username,
         name='Username Authentication'),

    path('api/profile/update-state/',
         general.update_profile_state, name='Update Profile State')


]
