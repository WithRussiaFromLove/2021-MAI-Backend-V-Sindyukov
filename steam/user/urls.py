from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('<int:user_id>/', get_user_by_id, name="get_user_by_id"),
#     path('<int:user_id>/purchase/', post_purchase, name="post_purchase"),
# ]