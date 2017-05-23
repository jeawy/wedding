from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 
urlpatterns = patterns('', 
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.txt$', TemplateView.as_view(template_name='sitemap.txt', content_type='text/plain')),
    url(r'^googleb9254da015a73344\.html$', TemplateView.as_view(template_name='googleb9254da015a73344.html', 
              content_type='text/plain')),
)
