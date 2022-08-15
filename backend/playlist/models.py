from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from xml.etree.ElementTree import tostring
from django.db import models
from django.db.models.deletion import CASCADE

from accounts.models import User

# class Playlist(models.Model):
#     # id = models.BigAutoField(primary_key=True)
#     created_by = models.ForeignKey(User, verbose_name='Created by', on_delete=models.CASCADE, db_column='created_by')
#     title = models.CharField(verbose_name='Playlist title', max_length=100, default=None)
#     jacket_pic = models.ImageField(verbose_name='Playlist jacket', upload_to='jackets/', blank=True, null=True)
#     description = models.TextField(verbose_name='Description', blank=True, null=True)
#     created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
#     is_private = models.BooleanField(verbose_name='Is private', default=False)

#     class Meta:
#         verbose_name = 'playlist'
#         verbose_name_plural = 'playlists'

#     def __str__(self):
#         return self.title

class Song(models.Model):
    title = models.CharField(verbose_name='Song title', max_length=255)
    artist = models.CharField(verbose_name='Artist', max_length=255)
    jacket = models.URLField(verbose_name='jacket_pic', null=True, blank=True)

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'
    
    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(verbose_name='name', max_length=10, unique=True, null=True)
    song = models.ManyToManyField(Song)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
    
    def __str__(self):
        return self.tag

class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, max_length=500)
    posted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return str(self.id)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    commentor = models.ForeignKey('accounts.User', verbose_name='Commentor', on_delete=models.SET_NULL, null=True)
    comment = models.TextField(verbose_name='Comment', max_length=255)
    parent = models.ForeignKey('self', verbose_name='Parent comment', on_delete = models.SET_NULL, null=True, related_name='parent_comment')
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
    
    def __str__(self):
        return self.id

# class Like(models.Model):
#     # id = models.AutoField(verbose_name='Like id', primary_key=True, unique=True)
#     liked_at = models.DateTimeField(verbose_name='Liked at', auto_now_add=True)
#     liker = models.ForeignKey('accounts.User', verbose_name='Liker', on_delete=models.SET_NULL, null=True)
#     playlist = models.ForeignKey(Song, verbose_name='Playlist', on_delete=models.CASCADE)

