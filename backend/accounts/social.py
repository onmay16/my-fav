from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser

from .serializers import FollowSerializer

from .models import Profile, Follow

@csrf_exempt
@permission_classes([IsAuthenticated])
def follow(request, nickname):
    if request.method == 'GET':
        user = request.user  # follower = logged in user
        profile_owner = Profile.objects.get(nickname=nickname).user  # following

        if user == profile_owner:
            return JsonResponse({'message':'Cannot follow yourself.'})
        else:
            new_follow = Follow(
                follower = user,
                following = profile_owner
            )
            new_follow.save()
            return JsonResponse({'message':'You have new connection now! :)'})

@csrf_exempt
@permission_classes([IsAuthenticated])
def follow_in_modal(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        user = request.user
        target_user = Profile.objects.get(nickname=data['nickname']).user

        new_follow = Follow(
            follower = user,
            following = target_user
        )
        new_follow.save()
        return JsonResponse({'message':'You have new connection now! :)'})

@csrf_exempt
@permission_classes([IsAuthenticated])
def unfollow(request, nickname):
    if request.method == 'GET':
        user = request.user # follower = logged in user
        profile_owner = Profile.objects.get(nickname=nickname).user # following

        exist_follow = Follow.objects.get(follower=user, following=profile_owner)
        exist_follow.delete()
        return JsonResponse({'message':'Successfully unfollowed.'})

@csrf_exempt
@permission_classes([IsAuthenticated])
def unfollow_in_modal(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        
        user = request.user
        target_user = Profile.objects.get(nickname=data['nickname']).user
        exist_follow = Follow.objects.get(follower=user, following=target_user)
        exist_follow.delete()
        return JsonResponse({'message':'Successfully unfollowed.'})

@csrf_exempt
def get_follow(request, nickname):
    if request.method == 'GET':
        profile_owner = Profile.objects.get(nickname=nickname).user

        followers = Follow.objects.select_related().filter(following=profile_owner)
        following = Follow.objects.select_related().filter(follower=profile_owner)

        return JsonResponse({'followers':FollowSerializer(followers).data, 'following':FollowSerializer(following).data})
        