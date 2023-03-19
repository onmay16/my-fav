from django.urls import path
from . import views, lastfm, song, search, feed

urlpatterns = [
    path('user/', views.user),
    path('search/artist/<str:artist>/', lastfm.search_artist),
    path('search/track/<str:track>/', lastfm.search_track),
    path('info/<str:artist>/<str:track>/', lastfm.getInfo_track),
    # path('add/', playlist.add_playlist),
    # path('edit/<int:id>/', playlist.edit_playlist),
    path('search/', search.search),
    path('post/', feed.add_post),
    path('post/<int:id>/edit/', feed.edit_post),
    path('post/<int:id>/delete/', feed.delete_post),
    path('main/', views.get_random_song)
]