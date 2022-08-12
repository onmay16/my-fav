from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.text import slugify
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe


import datetime

from rest_framework.authtoken.models import Token

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        Token.objects.get_or_create(user=user)
        return user
    
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(
            email,
            password=password,
        )

        user.is_admin = True
        user.is_active = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    # social account login
    LOGIN_TYPE_CHOICES = (
        ('gmail', 'Gmail'),
        ('apple', 'Apple'),
        ('facebook', 'Facebook'),
        ('kakaotalk', 'Kakaotalk')
    )

    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    date_of_birth = models.DateField(verbose_name='Date of birth', blank=True, null=True, default=datetime.date.today().strftime('%Y-%m-%d'))
    # login_type = models.CharField(verbose_name='User login type', max_length=20, choices=LOGIN_TYPE_CHOICES, blank=True, null=True)

    USERNAME_FIELD = 'email' # assign field for username
    REQUIRED_FIELDS = [] # set required fields

    objects = UserManager()

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last login', default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    playing_song = models.ForeignKey('playlist.Song', verbose_name='Now playing', blank=True, null=True, on_delete=models.SET_NULL)
    is_admin = models.BooleanField(verbose_name='Is admin', default=False)
    is_superuser = models.BooleanField(verbose_name='Is superuser', default=False)
    is_staff = models.BooleanField(verbose_name='Is staff', default=False)
    is_active = models.BooleanField(verbose_name='Is active', default=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name='User', on_delete=models.CASCADE)
    nickname = models.CharField(verbose_name='Nickname', max_length=20, unique=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture', upload_to='profiles/', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
    bio = models.TextField(verbose_name='Bio', null=True, blank=True)
    instagram = models.CharField(verbose_name='Instagram id', null=True, blank=True, max_length=16)
    slug = models.SlugField(max_length=20, blank=True, null=True)
    # follower = models.ManyToManyField(User, related_name='following')
    # following = models.ManyToManyField(User, related_name='follower')

    class Meta:
        verbose_name = 'profile'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return resolve_url("accounts:profile", self.slug)

    @property
    def profile_pic_tag(self):
        if self.profile_pic:
            return mark_safe('<img src="{}" width="150" height="150" />'.format(self.profile_pic.url))
        else:
            return 'No Image Found'



class Message(models.Model):
    # id = models.AutoField(verbose_name='Message id', primary_key=True, unique=True)
    sender = models.ForeignKey(User, verbose_name='Sender', related_name='receiver', on_delete=models.SET_NULL, null=True)
    receiver = models.ForeignKey(User, verbose_name='Receiver', related_name='sender', on_delete=models.SET_NULL, null=True)
    message = models.TextField(verbose_name='Message')
    sent_at = models.DateTimeField(verbose_name='Sent at', auto_now_add=True)
    read_at = models.DateTimeField(verbose_name='Read at', default=None)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

    def __str__(self):
        return self.id

class Follow(models.Model):
    # id = models.AutoField(verbose_name='Follow id', primary_key=True, unique=True)
    follower = models.ForeignKey(User, verbose_name='Follower', related_name='following', on_delete=models.CASCADE, null=True) # people who are following the 'following'
    following = models.ForeignKey(User, verbose_name='Following', related_name='follower', on_delete=models.CASCADE, null=True) # person who are followed by others

    class Meta:
        verbose_name = 'follow'
        verbose_name_plural = 'follows'
    
    def __str__(self):
        return self.id

class NotificationSender(models.Model):
    # notification = models.ForeignKey('Notification', verbose_name='Notifation', related_name='notification', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='From user', on_delete=models.SET_NULL, null=True)

class NotificationReceiver(models.Model):
    user = models.ForeignKey(User, verbose_name='To user', on_delete=models.SET_NULL, null=True)

class Notification(models.Model):
    NOTIFICATION_TYPE = (
        ('message', 'Message'),
        ('like', 'Like'),
        ('follow', 'Follow'),
        ('comment', 'Comment')
    )

    # id = models.AutoField(verbose_name='Notification id', primary_key=True, unique=True)
    from_user = models.ManyToManyField(NotificationSender, verbose_name='Notification from', related_name='to_user')
    to_user = models.ManyToManyField(NotificationReceiver, verbose_name='Notification to', related_name='from_user')
    # users = models.ManyToManyField(User, through=NoficationHelper, verbose_name='Nofication helper')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'
    
    def __str__(self):
        return self.id


