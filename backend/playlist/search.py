from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from .lastfm import search_artist, search_track

@permission_classes([IsAuthenticated])
def search(request):
    data = JSONParser().parse(request)
    category = data['category']

    if category == 'artist':
        return search_artist(data['artist'])
    else:
        # return search_track(data['title'])
        return search_track(data['title'])