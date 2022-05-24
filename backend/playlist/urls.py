from django.urls import path
from . import views, lastfm

urlpatterns = [
    path('main/', views.mainpage),
    path('search/artist/<str:artist>/', lastfm.search_artist),
    path('search/track/<str:track>/', lastfm.search_track),
    path('info/<str:artist>/<str:track>/', lastfm.getInfo_track),
    path('add/', views.add_playlist),
    path('edit/<int:id>/', views.edit_playlist),
]