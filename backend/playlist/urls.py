from django.urls import path
from . import views

urlpatterns = [
    path('search/artist/<str:artist>/', views.search_artist),
    path('search/track/<str:track>/', views.search_track),
]