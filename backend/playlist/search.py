from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from .lastfm import search_artist, search_track

@csrf_exempt
# @permission_classes([IsAuthenticated])
def search(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        category = data['category']

        if category == 'artist':
            # return search_artist(data['word'])
            return JsonResponse(search_artist(data['word']))
        else:
            return JsonResponse(search_track(data['word']))
            # return search_track(data['word'])