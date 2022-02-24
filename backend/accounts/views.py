import re
import json

from random import randint

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import Follow, User, Profile
from .serializers import ProfileSerializer, UserSerializer

from playlist.models import Playlist, Song, Genre
from playlist.serializers import PlaylistSerializer

from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
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

# @permission_classes([IsAuthenticated])
@csrf_exempt
def user_get_test(request):
    if request.method == 'POST':

        token = JSONParser().parse(request)['token']

        user = User.objects.get(auth_token=token)
        # profile = Profile.objects.all()
        profile = Profile.objects.select_related().get(user=request.user)
        # data = serializers.serialize('json', profile)
        print()

    # return JsonResponse({'data': data})
    return JsonResponse({'user':UserSerializer(user).data, 'profile':ProfileSerializer(profile).data})

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