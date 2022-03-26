from django.views.decorators.http import require_GET
from django.http import JsonResponse
import datetime


@require_GET
def get_purchase_by_id(request, purchase_id):
    return JsonResponse(
        {
            'id': purchase_id,
            'user': 'That User',
            'game': 'Game',
            'price': 1_000_000,
            'date': datetime.date(1997, 10, 19)
        }
    )


@require_GET
def get_adverts_by_game_id(request, game_id):
    return JsonResponse(
        {
            'game_id': game_id,
            'purchase': [
                {
                    'id': 1,
                    'user': 'That User',
                    'game': 'Game',
                    'price': 1_000_000,
                    'date': datetime.date(1997, 10, 19)
                },
                {
                    'id': 2,
                    'user': 'That User',
                    'game': 'Game',
                    'price': 1_200_000,
                    'date': datetime.date(1998, 10, 19)
                },
            ]
        }
    )