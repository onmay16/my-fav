import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend import my_settings

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
        artists[name] = {'mbid': '', 'url': ''}
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