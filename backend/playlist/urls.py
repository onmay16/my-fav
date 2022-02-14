from django.urls import path
from . import views

urlpatterns = [
    path('search/artist/<str:artist>/', views.search_artist),
    path('search/track/<str:track>/', views.search_track),
    path('info/<str:artist>/<str:track>/', views.getInfo_track)
]