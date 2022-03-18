# Generated by Django 4.0.2 on 2022-02-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_date_of_birth_alter_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True, verbose_name='Bio'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='insta_url',
            field=models.URLField(null=True, verbose_name='Instagram url'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2022-02-25', null=True, verbose_name='Date of birth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(default='2022-02-25 16:44:02', verbose_name='Last login'),
        ),
    ]
