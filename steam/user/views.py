from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from .models import *
from .serializers import LocationSerializer, UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

# @require_GET
# def get_user_by_id(request, user_id):
#     return JsonResponse(
#         {
#             'id': user_id,
#             'nickname': 'default',
#             'firstName': 'User',
#             'lastName': 'Last',
#             'email': 'user@email.com',
#             'location': 1234
#         }
#     )


# @csrf_exempt
# @require_POST
# def post_purchase(request, user_id):
#     return JsonResponse(
#         {
#             'code': 200,
#             'message': 'Advert was successfully saved'
#         }
#     )