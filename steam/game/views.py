from django.views.decorators.http import require_GET
from django.http import JsonResponse


@require_GET
def get_game_by_id(request, car_id):
    return JsonResponse(
        {
            'id': car_id,
            'name': 'RDR2',
            'genre': 'Action',
            'publisher': '2K'
        }
    )


@require_GET
def get_games_by_publisher(request, publisher):
    return JsonResponse(
        {
            'brand': publisher,
            'games': [
                {
                    'id': 1,
                    'name': 'RDR2',
                    'genre': 'Action',
                    'publisher': publisher
                },
                {
                    'id': 2,
                    'name': 'TLOU',
                    'genre': 'Action',
                    'publisher': publisher
                },
                {
                    'id': 3,
                    'name': 'Mario',
                    'genre': 'Platformer',
                    'publisher': publisher
                }
            ]
        }
    )


@require_GET
def get_games_by_genre_id(request, genre_id):
    return JsonResponse(
        {
            'category_id': genre_id,
            'category': 'Action',
            'cars': [
                {
                    'id': 1,
                    'name': 'RDR2',
                    'genre': 'Action',
                    'publisher': '2K'
                },
                {
                    'id': 2,
                    'name': 'TLOU',
                    'genre': 'Action',
                    'publisher': 'SONY'
                },
                {
                    'id': 3,
                    'name': 'GOW',
                    'genre': 'Action',
                    'publisher': 'SONY'
                }
            ]
        }
    )