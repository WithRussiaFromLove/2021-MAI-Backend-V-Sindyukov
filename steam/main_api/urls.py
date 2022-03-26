from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('game/', include('game.urls')),        # Game
    path('user/', include('user.urls')),      # User
    path('store/', include('store.urls')),  # Store
]