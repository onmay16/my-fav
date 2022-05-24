# Generated by Django 4.0.2 on 2022-02-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_bio_alter_profile_insta_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta_url',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram url'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default='2022-02-25 16:45:22', verbose_name='Last login'),
        ),
    ]