from django.urls import path
from .views import *

urlpatterns = [
    path('<int:purchase_id>/', get_purchase_by_id, name="get_purchase_by_id"),
    path('game/<int:game_id>', get_adverts_by_game_id, name="get_adverts_by_game_id"),
]