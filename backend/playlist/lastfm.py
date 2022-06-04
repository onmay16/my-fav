from unittest import result
import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from backend import my_settings

api_url = 'http://ws.audioscrobbler.com/2.0/'
api_key = my_settings.LASTFM_API_KEY

def get_result(url):
    result_data = requests.get(url).text
    fine_data = json.loads(result_data)
    return fine_data

def search_track(track):

    fine_data = get_result(f'{api_url}?method=track.search&format=json&track={track}&api_key={api_key}')

    # total_results = fine_data['results']['opensearch:totalResults']
    # items_per_page = fine_data['results']['opensearch:itemsPerPage']
    # total_pages = int(total_results)//int(items_per_page) + 1

    tracks = []
    # for pg in range(1, total_pages):
    #     fine_data = get_result(f'{api_url}?method=track.search&format=json&track={track}&page={pg}&api_key={api_key}')

    track_data = fine_data['results']['trackmatches']['track']

    for track in track_data:
        tracks.append({})
        tracks[-1]['name'] = track['name']
        tracks[-1]['artist'] = track['artist']
        tracks[-1]['url'] = track['url']
        tracks[-1]['mbid'] = track['mbid']

    return tracks
    

@csrf_exempt
def search_artist(artist):
    fine_data = get_result(f'{api_url}?method=artist.search&format=json&artist={artist}&api_key={api_key}')
    artist_data = fine_data['results']['artistmatches']['artist']

    artists = []

    for artist in artist_data:
        artists.append({})
        artists[-1]['name'] = artist['name']
        artists[-1]['mbid'] = artist['mbid']
        artists[-1]['url'] = artist['url']

    print(artists)

    return artists


def getInfo_track(artist, track):
    fine_data = get_result(f'{api_url}?method=track.getInfo&format=json&track={track}&artist={artist}&api_key={api_key}')

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


    return info