from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from administration import views

urlpatterns = patterns('user',
    #url(r'^$', views.index, name='index'),
    url(r'^portrait/$', views.portrait, name='portrait'), #
    url(r'^newgroup/$', views.newgroup, name='newgroup'), #
    url(r'^grouplist/$', views.grouplist, name='grouplist'), #
    url(r'^(?P<groupid>\d+)/modify_group/$', views.modify_group, name='modify_group'),
    #url(r'^modify_user/$', views.modify_user, name='modify_user'), #
    url(r'^(?P<userid>\d+)/modify_user/$', views.modify_user, name='modify_user'),
    url(r'^list_users/$', views.list_users, name='list_users'), #
    url(r'^admin_list_users/$', views.admin_list_users, name='admin_list_users'), #
    url(r'^upload_fake_portrait/$', views.upload_fake_portrait, name='upload_fake_portrait'), # 
    #url(r'^save_portrait/$', views.save_portrait, name='save_portrait'), #save portrait
    url(r'^usercenter/$', views.usercenter, name="usercenter")
) 


urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT ) 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT ) 
