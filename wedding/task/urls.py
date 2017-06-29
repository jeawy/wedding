from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from task import views

urlpatterns = patterns('task',  
    url(r'^todolist/$', views.todolist, name='todolist'),  
    url(r'^(?P<pk>\d+)/delitem/$', views.delitem, name='delitem'),  
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
