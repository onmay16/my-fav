from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:nickname>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('main/', views.mainpage),
]