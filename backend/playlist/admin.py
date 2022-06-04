from django.contrib import admin

from .models import Playlist, Song, Tag

# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'created_at', 'is_private')
    list_filter = ('created_by',)
    search_fields = ('created_by', )
    ordering = ('-created_at',)

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', )
    list_filter = ('title', 'artist', )
    search_fields = ('title', 'artist')
    ordering = ('title', 'artist', )

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     list_filter = ('name',)
#     search_fields = ('name',)


admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Genre, GenreAdmin)

# Register your models here.
