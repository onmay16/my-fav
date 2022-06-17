from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Post, Song
from .song import add_song

@csrf_exempt
@permission_classes([IsAuthenticated])
def add_post(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        new_post = Post(posted_by=request.user)
        track = data['track']
        artist = data['artist']
        content = data.get('content', None)

        try:
            song = Song.objects.get(title=track, artist=artist)
        except:
            song = add_song(track, artist)
        
        new_post.song = song
        if content:
            new_post.content = content
        
        new_post.save()
        return JsonResponse({'message':'Song is succesfully added to your feed.'})

@csrf_exempt
@permission_classes([IsAuthenticated])
def edit_post(request, id):
    if request.method == 'PUT':
        
        data = JSONParser().parse(request)
        post = Post.objects.get(id=id)
        content = data.get('content', None)

        if content:
            post.content = content
        else:
            post.content = None
        post.save()
        return JsonResponse({'message':'Successfully edited.'})

@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return JsonResponse({'message':'The song is succesfully deleted from your feed.'})

