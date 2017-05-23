from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from basedatas import views

urlpatterns = patterns('basedatas',
    url(r'^contact_us$', views.contact_us, name='contact_us'),   
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
