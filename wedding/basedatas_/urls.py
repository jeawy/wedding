from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from basedatas import views

urlpatterns = patterns('basedatas',
    url(r'^contact_us$', views.contact_us, name='contact_us'),  
    url(r'^user_register$', views.user_register, name='user_register'),  
    url(r'^find_password$', views.find_password, name='find_password'), 
    url(r'^reset_password$', views.reset_password, name='reset_password'), #reset password 
    url(r'^save_user$', views.save_user, name='save_user'),  
    url(r'^validate_username$', views.validate_username, name='validate_username'),
    url(r'^validate_uniqueness_email$', views.validate_uniqueness_email, name='validate_uniqueness_email'),
    url(r'^get_email_verify_code$', views.get_email_verify_code, name='get_email_verify_code'),
    url(r'^get_reset_pwd_verify_code$', views.get_reset_pwd_verify_code, name='get_reset_pwd_verify_code'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
