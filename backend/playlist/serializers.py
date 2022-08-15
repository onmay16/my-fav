from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Comment, Post, Song

# class PlaylistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Playlist
#         fields = ('created_by', 'title', 'jacket_pic', 'created_at', 'is_private')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'