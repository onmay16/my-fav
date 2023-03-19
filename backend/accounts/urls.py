from django.urls import path

from . import views, social

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('profile/<str:nickname>/', views.profile, name='profile'),
    path('follow/<str:nickname>/', social.follow),
    path('unfollow/<str:nickname>/', social.unfollow),
    path('profilebyid/', views.profile_by_id),
    path('followinmodal/', social.follow_in_modal),
    path('unfollowinmodal/', social.unfollow_in_modal),
]