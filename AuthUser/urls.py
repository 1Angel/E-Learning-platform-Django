from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('profile', views.userProfile, name='profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password-change'),
    path('information-change/', views.changeUserInfo, name='information-change'),

]