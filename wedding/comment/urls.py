from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from comment import views

urlpatterns = patterns('comment',
    url(r'^add_fresh/$', views.add_fresh, name='add_fresh'),
    url(r'^add_replied/$', views.add_replied, name='add_replied'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
