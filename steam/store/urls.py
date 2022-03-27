from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('', StoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('', post_purchase, name="post_purchase"),
#     path('all/', get_all_purchase, name="get_all_purchase"),
#     path('<int:purchase_id>/', get_purchase_by_id, name="get_purchase_by_id"),
#     path('game/<int:game_id>', get_adverts_by_game_id, name="get_adverts_by_game_id"),
# ]
