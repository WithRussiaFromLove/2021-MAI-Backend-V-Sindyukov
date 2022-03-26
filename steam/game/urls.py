from django.urls import path
from .views import *

urlpatterns = [
    path('<int:car_id>/', get_game_by_id, name="get_game_by_id"),
    path('publisher/<str:publisher_name>/', get_games_by_publisher, name="get_games_by_publisher"),
    path('genre/<str:genre_id>/', get_games_by_genre_id, name="get_games_by_genre_id"),
]