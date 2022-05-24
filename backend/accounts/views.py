import re

from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

from .models import Follow, User, Profile
from .serializers import ProfileSerializer, UserSerializer

from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer

from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        email = data['email']

        if re.search('(@.*\.)', email) == None:
            return JsonResponse({'message': 'Please enter valid email address.'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'message': 'This mail address has been taken.'})
        
        if data['password1'] != data['password2']:
            return JsonResponse({'message': 'Passwords do not match.'})

        user = User.objects.create_user(email=data['email'], password=data['password1'])
        try:
            profile = Profile(user=user, nickname=data['nickname'])
        except:
            profile = Profile(user=user, nickname=f'user{user.id}')
        
        user.save()
        profile.save()
        token = user.auth_token.key
        nickname = profile.nickname
        login(request, user)
        
        return JsonResponse({'Token': token, 'message':('Welcome! 🥳 ' + nickname)}, status=200)

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # user = authenticate(email=data['email'], password=data['password'])
        try:
            user = User.objects.get(email=data['email'])
        except:
            return JsonResponse({'message':'User does not exist'})

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

@permission_classes([IsAuthenticated])
def signout(request):
    if request.method == 'GET':
        nickname = Profile.objects.get(user=request.user).nickname
        # print(request.user)
        # print(request.user.auth_token.key)
        request.user.auth_token.delete()
        logout(request)

        return JsonResponse({'message':('See you Soon, ' + nickname)}, status=200)

@csrf_exempt
@permission_classes([IsAuthenticated])
def profile(request, nickname):
    user = request.user
    try:
        profile = Profile.objects.get(nickname=nickname)
    except:
        return JsonResponse({'message':'User does not exist.'})

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
        data = JSONParser().parse(request)
        profile_user= profile.user

        if request.user != profile_user:
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