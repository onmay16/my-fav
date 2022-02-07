from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.expressions import OrderBy

from .models import Follow, Message, Notification, User, Profile

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'date_of_birth', 'created_at', 'last_login', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', )
    ordering = ('-created_at',)
    filter_horizontal = ()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'updated_at', 'bio', 'insta_url')
    search_fields = ('nickname',)
    ordering = ('-updated_at',)
    prepopulated_fields = {'slug': ('nickname', )}

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message', 'sent_at', 'read_at')
    list_filter = ('sender', 'receiver', 'sent_at')
    search_fields = ('sender', 'receiver')
    ordering = ('-sent_at',)

# class FollowAdmin(admin.ModelAdmin):
#     list_display = ('id', 'follower', 'following')
#     list_filter = ('follower', 'following')
#     search_fields = ('follower', 'following')

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'from_user', 'to_user', 'like_type')
#     list_filter = ('from_user', 'to_user', 'like_type')
#     search_fields = ('from_user', 'to_user', 'like_type')
#     ordering = ('-created_at',)


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
admin.site.register(Message, MessageAdmin)
# admin.site.register(Follow, FollowAdmin)
# admin.site.register(Notification, NotificationAdmin)

