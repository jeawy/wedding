from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from msg import views

urlpatterns = patterns('msg',
    url(r'^$', views.index, name='index'),  
    url(r'^add/$', views.add, name='add'), #save
    url(r'^(?P<msg_id>\d+)/delete/$', views.delete, name='delete'), 
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
