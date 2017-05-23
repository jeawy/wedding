from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from good import views

urlpatterns = patterns('good', 
    url(r'^add/$', views.add, name='add'),
    url(r'^del/$', views.delele, name='del'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
