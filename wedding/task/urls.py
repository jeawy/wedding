from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from task import views

urlpatterns = patterns('task', 
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<taskid>\d+)/detail/$', views.detail, name='detail'),
    url(r'^deltest/$', views.deltest, name='del'),
    url(r'^todolist/$', views.todolist, name='todolist'), # 
    url(r'^(?P<taskid>\d+)/change/$', views.change, name='change'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
