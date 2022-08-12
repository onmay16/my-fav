from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

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
def unfollow(request, nickname):
    if request.method == 'GET':
        user = request.user # follower = logged in user
        profile_owner = Profile.objects.get(nickname=nickname).user # following

        exist_follow = Follow.objects.get(follower=user, following=profile_owner)
        exist_follow.delete()
        return JsonResponse({'message':'Successfully unfollowed.'})
