from django.urls import path
from .views import *


urlpatterns = [
    path('profile/<int:profile_id>/', get_profile, name="get_profile"),  # Get User Profile
    path('game/<int:game_id>/', get_game, name="get_game"),
    path('all/', get_games, name="get_games"),
    path('category/<str:category>/', get_category, name="get_category"),
]