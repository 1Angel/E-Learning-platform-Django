from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:id>', views.details, name='course'),
    path('course/<int:pk>/section/<int:id>', views.sectionDetail, name='section'),

]