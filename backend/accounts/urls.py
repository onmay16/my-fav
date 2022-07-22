from django.urls import path

from . import views, social

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('profile/<str:nickname>/', views.profile, name='profile'),
    path('follow/<str:nickname>/', social.follow),
]