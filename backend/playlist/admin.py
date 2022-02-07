from django.contrib import admin

from .models import Genre, Playlist, Song, Tag

# Register your models here.

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'created_at', 'is_private')
    list_filter = ('created_by',)
    search_fields = ('created_by', )
    ordering = ('-created_at',)

# class SongAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'artist', 'date_released', 'length', 'album')
#     list_filter = ('title', 'artist', 'album')
#     search_fields = ('title', 'artist')
#     ordering = ('title', 'artist', '-date_released')

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    list_filter = ('tag',)
    search_fields = ('tag',)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre',)
    list_filter = ('genre',)
    search_fields = ('genre',)


admin.site.register(Playlist, PlaylistAdmin)
# admin.site.register(Song, SongAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Genre, GenreAdmin)

# Register your models here.
