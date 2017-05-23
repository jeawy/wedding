from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from tools import views

urlpatterns = [  
    url(r'^create_thumbnail/$', views.create_thumbnail, name='create_thumbnail'),
]
