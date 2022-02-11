import re
import json
from random import randint

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.test import tag
from django.views.decorators.csrf import csrf_exempt

from .models import Follow, User, Profile
from .serializers import ProfileSerializer, UserSerializer

from playlist.models import Playlist, Song, Tag
from playlist.serializers import PlaylistSerializer

from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes

# Create your views here.

@csrf_exempt
def signup(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']

        if re.search('(@.*\.)', email) == None:
            return JsonResponse({'message': 'Please enter valid email address.'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'User already exist.'})
        
        if data['password1'] != data['password2']:
            return JsonResponse({'message': 'Passwords do not match.'})

        user = User.objects.create_user(email=data['email'], password=data['password1'])
        profile = Profile(user=user, nickname=data['nickname'])

        user.save()
        profile.save()
        token = user.auth_token.key
        nickname = profile.nickname
        
        return JsonResponse({'Token': token, 'message':('Welcome! 🥳 ' + nickname)}, status=200)

@csrf_exempt
# @permission_classes([AllowAny])
def signin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(email=data['email'], password=data['password'])

        if user:
            if user.is_active:
                login(request, user)
                token = Token.objects.get_or_create(user=user)[0].key
                profile = Profile.objects.get(user=user)
                nickname = profile.nickname

                return JsonResponse({
                    'Token': token,
                    'User': UserSerializer(user).data, 
                    'message':('Welcome back, '+ nickname +'!')}, 
                    status=200)
            else:
                return JsonResponse({'message':'User is not active'})
        else:
            return JsonResponse({'message':'User does not exist'})

@permission_classes([IsAuthenticated])
def signout(request):
    if request.method == 'GET':
        nickname = Profile.objects.get(user=request.user).nickname
        # print(request.user)
        # print(request.user.auth_token.key)
        request.user.auth_token.delete()
        logout(request)

        return JsonResponse({'message':('See you Soon, ' + nickname)}, status=200)

@permission_classes([IsAuthenticated])
def mainpage(request):

    def get_random_idx(obj, start):
        total = obj.objects.all().count()
        print('total: ' + str(total))
        random_idx = randint(start, total)
        return random_idx
    
    def tag_dic(tag_lst, dic={}):
        for tag in tag_lst:
            if tag.tag in dic:
                dic[tag.tag] =+ 1
            else:
                dic[tag.tag] = 1
        return dic

    def tag_lst(songs, lst=[]):
        for song in songs:
            tags = Tag.objects.select_related().filter(song=song)
            lst.extend(tags)
        return lst
    
    def song_list(playlists, lst=[]):
        for playlist in playlists:
            songs = Song.objects.select_related().filter(playlist=playlist)
            lst.extend(songs)
        return lst

    if request.method == 'GET':
        user = request.user
        nickname = Profile.objects.get(user=user).nickname
        
        # user recommendation section
        first_user_idx = get_random_idx(User, 2)
        second_user_idx = get_random_idx(User, 2)

        while ((first_user_idx == user.id)):
            first_user_idx = get_random_idx(User, 2)
        while ((first_user_idx == second_user_idx) or (second_user_idx == user.id)):
            second_user_idx = get_random_idx(User, 2)

        first_user = User.objects.get(id=first_user_idx)
        first_profile = Profile.objects.get(user=first_user)
        first_playlists = Playlist.objects.filter(created_by=first_user)
        first_tags = tag_dic(tag_lst(song_list(first_playlists)))

        second_user = User.objects.get(id=second_user_idx)
        second_profile = Profile.objects.get(user=second_user)
        second_playlists = Playlist.objects.filter(created_by=second_user)
        second_tags = tag_dic(tag_lst(song_list(second_playlists)))

        # tag recommendation section
        first_tag_idx = get_random_idx(Tag, 1)
        second_tag_idx = get_random_idx(Tag, 1)

        while ((first_tag_idx == second_tag_idx)):
            second_tag_idx = get_random_idx(Tag, 1)
        
        first_tag = Tag.objects.get(id=first_tag_idx)
        second_tag = Tag.objects.get(id=second_tag_idx)
        
        # Playlist recommendation section
        first_playlist_idx = get_random_idx(Playlist, 1)
        second_playlist_idx = get_random_idx(Playlist, 1)

        while ((first_playlist_idx == second_playlist_idx)):
            second_playlist_idx = get_random_idx(Playlist, 1)

        first_playlist = Playlist.objects.get(id=first_playlist_idx)
        second_playlist = Playlist.objects.get(id=second_playlist_idx)

        return JsonResponse({
            'First user': UserSerializer(first_user).data,
            'First user\'s profile': ProfileSerializer(first_profile).data,
            'First user\'s tags': json.dumps(first_tags),
            'Second user': UserSerializer(second_user).data,
            'Second user\'s profile': ProfileSerializer(second_profile).data,
            'Second user\'s tags': json.dumps(second_tags),
            'First tag': first_tag.tag,
            'Second tag': second_tag.tag,
            'First_playlist': PlaylistSerializer(first_playlist).data,
            'Second_playlist': PlaylistSerializer(second_playlist).data
        })

@permission_classes([IsAuthenticated])
def profile(request, nickname):

    profile = Profile.objects.get(nickname=nickname)
    user = profile.user

    if request.method == 'GET':

        playlists = Playlist.objects.select_related().filter(created_by=user.id)
        following = Follow.objects.select_related().filter(follower=user).count()
        follower = Follow.objects.select_related().filter(following=user).count()

        return JsonResponse({
            'message':(nickname + "'s profile page"),
            'Profile info': ProfileSerializer(profile).data,
            'User info': UserSerializer(user).data,
            'Playlist': PlaylistSerializer(playlists, many=True).data,
            'Following': following,
            'Follower': follower}, 
            status=200)

    if request.method == 'POST':
        
        # response = HttpResponse()
        # csrftoken = csrf.get_token(request)
        # print('csrf:' + csrftoken)

        data = JSONParser().parse(request)

        if request.user != user:
            return JsonResponse({'message':'Authorization is needed to edit profile.'})
        else:
            nickname = data.get('nickname', None)
            profile_pic = data.get('profile_pic', None)
            bio = data.get('bio', None)
            instagram = data.get('instagram', None)
            
            if nickname != None:
                profile.nickname = nickname
            if profile_pic != None:
                profile.profile_pic = profile_pic
            if bio != None:
                profile.bio = bio
            if instagram != None:
                profile.insta_url = 'https://www.instagram.com/' + instagram
            
            profile.save()
            return JsonResponse({'message':'Profile is successfully updated.'})