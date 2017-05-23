from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from statistics import views

urlpatterns = patterns('statistics',
    url(r'^$', views.dashboard, name='dashboard'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
