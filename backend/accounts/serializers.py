# from django.db.models import fields
from typing_extensions import Required
from rest_framework import serializers
from .models import Profile, User, Message, Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

class ProfileSerializer(serializers.ModelSerializer):

    profile_pic = serializers.ImageField(required = False)

    class Meta:
        model = Profile
        fields = ('nickname', 'profile_pic', 'instagram', 'bio')

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
