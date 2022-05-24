from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('profile/<str:nickname>/', views.profile, name='profile'),
]