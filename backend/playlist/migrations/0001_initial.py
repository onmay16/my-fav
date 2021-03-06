# Generated by Django 4.0.2 on 2022-02-06 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='Playlist title')),
                ('jacket_pic', models.ImageField(blank=True, null=True, upload_to='jackets/', verbose_name='Playlist jacket')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('is_private', models.BooleanField(default=False, verbose_name='Is private')),
                ('created_by', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'playlist',
                'verbose_name_plural': 'playlists',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Song title')),
                ('artist', models.CharField(max_length=255, verbose_name='Artist')),
                ('deate_released', models.DateField(blank=True, null=True, verbose_name='Date released')),
                ('length', models.DurationField(verbose_name='Song duration')),
                ('album_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Album title')),
                ('playlist', models.ManyToManyField(to='playlist.Playlist')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10, unique=True, verbose_name='Tag')),
                ('song', models.ManyToManyField(to='playlist.Song')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True, verbose_name='Liked at')),
                ('liker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Liker')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.playlist', verbose_name='Playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Genre')),
                ('song', models.ManyToManyField(to='playlist.Song')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('commentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Commentor')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_comment', to='playlist.comment', verbose_name='Parent comment')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlist.playlist', verbose_name='Playlist')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
