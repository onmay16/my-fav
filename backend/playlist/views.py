import random

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser

from .models import Song, Post
from .serializers import PostSerializer, SongSerializer

from accounts.models import Profile
from accounts.serializers import UserSerializer, ProfileSerializer

@csrf_exempt
@permission_classes([IsAuthenticated])
def user(request):

    if request.method == 'GET':
        user = request.user
        profile = Profile.objects.get(user=user)
        print(ProfileSerializer(profile).data)

        return JsonResponse({'user':UserSerializer(user).data, 'profile':ProfileSerializer(profile).data})


@csrf_exempt
def get_random_song(request):

    if request.method == 'GET':
        posts = list(Post.objects.all())
        try:
            random_posts = random.sample(posts, 4)
        except:
            total = len(posts)
            random_posts = random.sample(posts, total)
        songs = []
        users = []
        for post in random_posts:
            songs.append(Song.objects.get(id=post.song.id))
            users.append(Profile.objects.get(user=post.posted_by))


        return JsonResponse({'songs':SongSerializer(songs, many=True).data, 'posts': PostSerializer(random_posts, many=True).data, 'users': ProfileSerializer(users, many=True).data})
