from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('achievements/',views.achievements, name='achievements'),
    path('projects/',views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]