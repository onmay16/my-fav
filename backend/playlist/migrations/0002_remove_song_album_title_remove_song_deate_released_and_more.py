# Generated by Django 4.0.2 on 2022-02-12 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album_title',
        ),
        migrations.RemoveField(
            model_name='song',
            name='deate_released',
        ),
        migrations.RemoveField(
            model_name='song',
            name='length',
        ),
    ]
