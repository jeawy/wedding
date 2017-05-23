from django.conf.urls import url

from data import views

urlpatterns = [
    url(r'^latest_kb/$', views.latest_kb, name="latest_kb"),
    # 
    url(r'^map/$', views.map, name="map"),
    url(r'^week_recommend_kb/$', views.week_recommend_kb, name="week_recommend_kb"),
    url(r'^api/update_data_place/$', views.update_data_place , name="update_data_place"),
    url(r'^api/update_data_place_rate/$', views.update_data_place_rate , name="update_data_place_rate"), 
]