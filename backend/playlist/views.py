import imp
from urllib import response
from httplib2 import Response
import requests
import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models.aggregates import Count

from backend import my_settings
from random import randint

from rest_framework.parsers import JSONParser
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .serializers import PlaylistSerializer
from .models import Playlist, Genre, Song
from accounts.models import User, Profile, Follow
from accounts.serializers import UserSerializer, ProfileSerializer




# Create your views here.

api_url = 'http://ws.audioscrobbler.com/2.0/'
api_key = my_settings.LASTFM_API_KEY

@csrf_exempt
def search_artist(request, artist):
        
    url = api_url+'?method=artist.search&format=json&artist='+artist+'&api_key='+api_key
    result_data = requests.get(url).text
    fine_data = json.loads(result_data)
    artist_data = fine_data['results']['artistmatches']['artist']
    artists = {}

    for artist in artist_data:
        name = artist['name']
        artists[name] = {'mbid':'', 'url':''}
        artists[name]['mbid'] = artist['mbid']
        artists[name]['url'] = artist['url']

    return JsonResponse({'artists': artists}) 

def search_track(request, track):

    url = api_url+'?method=track.search&format=json&track='+track+'&api_key='+api_key
    
    result_data = requests.get(url).text
    fine_data = json.loads(result_data)
    track_data = fine_data['results']['trackmatches']['track']

    tracks = {}
    for track in track_data:
        name = track['name']
        tracks[name] = {'artist':'', 'url':'', 'mbid':''}
        tracks[name]['artist'] = track['artist']
        tracks[name]['url'] = track['url']
        tracks[name]['mbid'] = track['mbid']

    return JsonResponse({'tracks': tracks})

def getInfo_track(request, artist, track):
    
    url = api_url + '?method=track.getInfo&format=json&track='+track+'&artist='+artist+'&api_key='+api_key
    
    result_data = requests.get(url).text
    fine_data = json.loads(result_data)
    info_data = fine_data['track']

    info = {
        'name':info_data['name'], 
        'url':info_data['url'],
        'artist':info_data['artist']['name'],
        'artist_url':info_data['artist']['url'],
        'tags':[]
        }
    
    for tag in info_data['toptags']['tag']:
        info['tags'].append(tag['name'])
    
    return JsonResponse({'info': info})
    # return JsonResponse({'data': info_data})

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



    
    
    
    
    