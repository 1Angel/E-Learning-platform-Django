from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.AllCourses, name='courses'),
    path('dashboard/create', views.CreateCourse, name='create'),
    path('course/<int:id>', views.details, name='course'),
    path('search', views.searchCourses, name='search'),
    path('course/<int:pk>/section/<int:id>', views.sectionDetail, name='section'),

]