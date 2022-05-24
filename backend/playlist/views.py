from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from random import randint

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser

from .models import Playlist, Song
from .serializers import PlaylistSerializer
from accounts.models import User, Profile
from accounts.serializers import UserSerializer, ProfileSerializer

@permission_classes([IsAuthenticated])
def mainpage(request):

    def get_random_idx(obj, start):
        total = obj.objects.all().count()
        # print('total: ' + str(total))
        random_idx = randint(start, total)
        return random_idx
    
    def song_list(playlists, lst=[]):
        for playlist in playlists:
            songs = Song.objects.select_related().filter(playlist=playlist)
            lst.extend(songs)
        return lst

    if request.method == 'GET':
        # user = request.user
        # nickname = Profile.objects.get(user=user).nickname
        
        # user recommendation section
        first_user_idx = get_random_idx(User, 2)
        second_user_idx = get_random_idx(User, 2)

        # while ((first_user_idx == user.id)):
        #     first_user_idx = get_random_idx(User, 2)
        while (first_user_idx == second_user_idx):
            # or (second_user_idx == user.id))
            second_user_idx = get_random_idx(User, 2)

        first_user = User.objects.get(id=first_user_idx)
        first_profile = Profile.objects.get(user=first_user)
        # first_playlists = Playlist.objects.filter(created_by=first_user)
        # first_songs = song_list(first_playlists)

        second_user = User.objects.get(id=second_user_idx)
        second_profile = Profile.objects.get(user=second_user)
        # second_playlists = Playlist.objects.filter(created_by=second_user)

        # genre recommendation section
        # first_genre_idx = get_random_idx(Genre, 1)
        # second_genre_idx = get_random_idx(Genre, 1)

        # while ((first_genre_idx == second_genre_idx)):
        #     second_genre_idx = get_random_idx(Genre, 1)
        
        # first_genre = Genre.objects.get(id=first_genre_idx)
        # first_genre= Genre.objects.get(id=second_genre_idx)
        
        # # Playlist recommendation section
        # first_playlist_idx = get_random_idx(Playlist, 1)
        # second_playlist_idx = get_random_idx(Playlist, 1)

        # while ((first_playlist_idx == second_playlist_idx)):
        #     second_playlist_idx = get_random_idx(Playlist, 1)

        # first_playlist = Playlist.objects.get(id=first_playlist_idx)
        # second_playlist = Playlist.objects.get(id=second_playlist_idx)

        return JsonResponse({
            'first_user': UserSerializer(first_user).data,
            'first_profile': ProfileSerializer(first_profile).data,
            'second_user': UserSerializer(second_user).data,
            'second_profile': ProfileSerializer(second_profile).data,
            # 'First genre': first_genre.genre,
            # 'Second genre': first_genre.genre,
            # 'First_playlist': PlaylistSerializer(first_playlist).data,
            # 'Second_playlist': PlaylistSerializer(second_playlist).data
        })

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



    
    
    
    
    