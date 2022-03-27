from django.views.decorators.http import require_GET, require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
from rest_framework import viewsets

from .models import *
from .serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all().order_by('id')
    serializer_class = StoreSerializer

# @require_GET
# def get_purchase_by_id(request, purchase_id):
#     return JsonResponse(
#         {
#             'id': purchase_id,
#             'user': 'That User',
#             'game': 'Game',
#             'price': 1_000_000,
#             'date': datetime.date(1997, 10, 19)
#         }
#     )


# @require_GET
# def get_adverts_by_game_id(request, game_id):
#     return JsonResponse(
#         {
#             'game_id': game_id,
#             'purchase': [
#                 {
#                     'id': 1,
#                     'user': 'That User',
#                     'game': 'Game',
#                     'price': 1_000_000,
#                     'date': datetime.date(1997, 10, 19)
#                 },
#                 {
#                     'id': 2,
#                     'user': 'That User',
#                     'game': 'Game',
#                     'price': 1_200_000,
#                     'date': datetime.date(1998, 10, 19)
#                 },
#             ]
#         }
#     )

# @require_GET
# def get_all_purchase(request):
#     return JsonResponse(
#         {
#             'purchase': [
#                 {
#                     'id': 1,
#                     'user': 'That User',
#                     'game': 'Game',
#                     'price': 1_200_000,
#                     'date': datetime.date(1998, 10, 19)
#                 },
#                 {
#                     'id': 2,
#                     'user': 'User That',
#                     'game': 'Emag',
#                     'price': 1_300_000,
#                     'date': datetime.date(1999, 10, 19)
#                 }
#             ]
#         }
#     )

# @csrf_exempt
# @require_POST
# def post_purchase(request):
#     return JsonResponse(
#         {
#             'code': 200,
#             'message': f'purchase was successfully published'
#         }
#     )