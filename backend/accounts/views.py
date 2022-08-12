import re
from telnetlib import STATUS

from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt

from .models import Follow, User, Profile
from .serializers import ProfileSerializer, UserSerializer

from playlist.models import Post, Song
from playlist.serializers import PostSerializer, SongSerializer

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
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
        authenticateduser = authenticate(request, email=data['email'], password=data['password'])
        login(request, authenticateduser)
        
        return JsonResponse({'Token': token, 'message':('Welcome! 🥳 ' + nickname)}, status=200)

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # user = authenticate(email=data['email'], password=data['password'])
        try:
            user = User.objects.get(email=data['email'])
        except:
            return JsonResponse({'message':'User does not exist'}, status=404, )

        if user.is_active:
            authenticateduser = authenticate(request, email=data['email'], password=data['password'])
            if user is not None:
                login(request, authenticateduser)
                token = Token.objects.get_or_create(user=user)[0].key
                profile = Profile.objects.get(user=user)
                nickname = profile.nickname

                return JsonResponse({
                    'Token': token,
                    'User': UserSerializer(user).data,
                    'message': ('Welcome back, ' + nickname + '!')},
                    status=200)
            else:
                return JsonResponse({'message':'Check your password'}, status=401)
        else:
            return JsonResponse({'message':'User is not active'}, status=404)

@permission_classes([IsAuthenticated])
def signout(request):
    
    nickname = Profile.objects.get(user=request.user).nickname
    # print(request.user)
    # print(request.user.auth_token.key)
    request.user.auth_token.delete()
    logout(request)

    return JsonResponse({'message':('See you Soon, ' + nickname)}, status=200)

@csrf_exempt
@permission_classes([IsAuthenticated])
def profile(request, nickname):

    # parser_classes = (MultiPartParser, FormParser)

    user = request.user
    try:
        profile = Profile.objects.get(nickname=nickname)
        print(profile)
    except:
        return JsonResponse({'message':'User does not exist.'})

    if request.method == 'GET':

        following = Follow.objects.select_related().filter(follower=profile.user).count()
        follower = Follow.objects.select_related().filter(following=profile.user).count()
        user = request.user
        posts = Post.objects.filter(posted_by=profile.user)
        number_of_posts = Post.objects.filter(posted_by=user).count()
        
        if Follow.objects.select_related().filter(follower=user, following=profile.user).count() == 1:
            is_following = True
        elif Follow.objects.select_related().filter(follower=user, following=profile.user).count() == 0:
            is_following = False
        else:
            return JsonResponse({'message':'Cannot find any information about social activity.'})

        song_list = []
        for post in posts.values():
            song = Song.objects.get(id=post['song_id'])
            song_list.append(song)

        return JsonResponse({
            'message':(nickname + "'s profile page"),
            'profile': ProfileSerializer(profile).data,
            'user': UserSerializer(user).data,
            'following': following,
            'follower': follower,
            'len':number_of_posts, 
            'posts':PostSerializer(posts, many=True).data,
            'songs':SongSerializer(song_list, many=True).data,
            'is_following': is_following},
            status=200)

    if request.method == 'POST':

        print(request.body)
        
        data = JSONParser().parse(request)
        print(data)

        profile_user= profile.user

        if request.user != profile_user:
            return JsonResponse({'message':'Authorization is needed to edit profile.'})
        # elif data.is_valid():
        #     data.save()
        #     return JsonResponse({'message':'Profile is successfully updated.'})
        # else:
        #     return JsonResponse({'message':'Fail to update your profile.'})

        else:
            nickname = data.get('nickname', profile.nickname)
            bio = data.get('bio', None)
            instagram = data.get('instagram', profile.instagram)
            # profile_pic = request.FILES.get('profile_pic', profile.profile_pic)

            # if:
            #     profile_pic = request.FILES['profile_pic']
            # else:
            #     profile_pic = profile.profile_pic
            
            
            if nickname != None:
                profile.nickname = nickname
            # if profile_pic != None:
            #     profile.profile_pic = profile_pic
            if bio != None:
                profile.bio = bio
            if instagram != None:
                profile.instagram = instagram
            
            profile.save()
            return JsonResponse({'message':'Profile is successfully updated.'})
            