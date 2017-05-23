from django.conf.urls import include, url 
from search import views


urlpatterns = [
    url(r'^inplace/$', views.inplace, name='inplace'),
    url(r'^search_all/$', views.search_all, name='search_all'),
    url(r'^search_records/$', views.search_records, name='search_records'),
    url(r'^test_search/$', views.test_search, name='test_search'),
]