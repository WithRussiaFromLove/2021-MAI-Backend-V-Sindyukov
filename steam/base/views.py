from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import *
from random import randint

# Create your views here.
MAX_ID = 100_000


@require_GET
def get_profile(request, profile_id):
    return JsonResponse(
        {
            'id': profile_id,
            'firstName': 'User',
            'lastName': 'Gaben',
            'about': 'I dont like number 3.'
        }
    )

@require_GET
def get_game(request, game_id):
    return JsonResponse(
        {
            'id': game_id,
            'name': 'Name',
            'studio': 'Brand',
            'genre': 'FPS',
            'year': 2022,
        }
    )

@require_GET
def get_games(request):
    return JsonResponse(
        {
            'games': [
                {
                    'id': randint(0, MAX_ID),
                    'name': 'Battlefield',
                    'studio': 'EA',
                    'genre': 'FPS',
                    'year': 2022,
                },
                {
                    'id': randint(0, MAX_ID),
                    'name': 'Civilization',
                    'studio': '2K',
                    'genre': 'RTS',
                    'year': 2018,
                },
                {
                    'id': randint(0, MAX_ID),
                    'name': 'Forza Horizon 4',
                    'studio': 'Playground',
                    'genre': 'racing',
                    'year': 2018,
                }
            ]
        }
    )

@require_GET
def get_category(request, category):
    return JsonResponse(
        {
            'category': category,
            'description': 'Category description',
            'positions': [
                {
                    'id': randint(0, MAX_ID),
                    'name': 'Dying light',
                    'studio': 'Techland',
                    'genre': 'Action',
                    'year': 2015,
                },
                {
                    'id': randint(0, MAX_ID),
                    'name': 'Halo',
                    'studio': '343i',
                    'genre': 'FPS',
                    'year': 2022,
                },
                {
                    'id': randint(0, MAX_ID),
                    'name': 'GTA 4',
                    'studio': '2K',
                    'genre': 'Action',
                    'year': 2008,
                }
            ]
        }
    )