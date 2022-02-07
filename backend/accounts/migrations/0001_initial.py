# Generated by Django 4.0.2 on 2022-02-06 22:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('date_of_birth', models.DateField(blank=True, default='2022-02-06', null=True, verbose_name='Date of birth')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('last_login', models.DateTimeField(default='2022-02-06 16:20:31', verbose_name='Last login')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is superuser')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='Nickname')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/', verbose_name='Profile Picture')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('bio', models.TextField(verbose_name='Bio')),
                ('insta_url', models.URLField(verbose_name='Instagram url')),
                ('slug', models.SlugField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'profile',
            },
        ),
        migrations.CreateModel(
            name='NotificationSender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='From user')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationReceiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='To user')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('message', 'Message'), ('like', 'Like'), ('follow', 'Follow'), ('comment', 'Comment')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('from_user', models.ManyToManyField(related_name='to_user', to='accounts.NotificationSender', verbose_name='Notification from')),
                ('to_user', models.ManyToManyField(related_name='from_user', to='accounts.NotificationReceiver', verbose_name='Notification to')),
            ],
            options={
                'verbose_name': 'notification',
                'verbose_name_plural': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Sent at')),
                ('read_at', models.DateTimeField(default=None, verbose_name='Read at')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Follower')),
                ('following', models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Following')),
            ],
            options={
                'verbose_name': 'follow',
                'verbose_name_plural': 'follows',
            },
        ),
    ]
