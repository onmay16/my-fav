from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from .models import Playlist
from .serializers import PlaylistSerializer

@csrf_exempt
@permission_classes([IsAuthenticated])
def add_playlist(request):
    if request.method == 'POST':
        
        data = JSONParser().parse(request)

        new_playlist = Playlist()
        
        title = data['title']
        jacket= data.get('jacket', None)
        description = data.get('description', None)
        is_private = data.get('is_private', None)

        new_playlist.created_by = request.user
        if not title or title.isspace():
            return JsonResponse({'message':'Please title your playlist.'})
        new_playlist.title = title
        if jacket != None:
            new_playlist.jacket_pic = jacket
        if description != None:
            new_playlist.description = description
        if is_private != None:
            new_playlist.is_private = is_private

        new_playlist.save()
        return JsonResponse({'message':'New playlist is successfully added.', 'added playlist':PlaylistSerializer(new_playlist).data})

@csrf_exempt
@permission_classes([IsAuthenticated])
def edit_playlist(request, id):
    playlist = Playlist.objects.get(id=id)
    if request.method == 'PUT':
        
        data = JSONParser().parse(request)

        title = data.get('title', None)
        jacket= data.get('jacket', None)
        description = data.get('description', None)
        is_private = data.get('is_private', None)

        if title != None:
            playlist.title = title
        if jacket != None:
            playlist.jacket_pic = jacket
        if description != None:
            playlist.description = description
        if is_private != None:
            playlist.is_private = is_private

        playlist.save()
        return JsonResponse({'messsage':'Playlist has been successfully updated.'})

    elif request.method == 'DELETE':

        playlist.delete()
        return JsonResponse({'messsage':'Playlist has been successfully deleted.'})

# @permission_classes([IsAuthenticated])
# def add_songs(request, id, song):
#     playlist = Playlist.objects.get(id=id)
#     # add songs to playlist
#     if request.method == 'POST':
#         try:
#             song = Song.objects.get()


# def delete_songs(request, id):
#     # delete songs from playlist
#     if request.method == 'DELETE':