from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from kb import views

urlpatterns = patterns('kb',
    url(r'^newkb/$', views.newkb, name='newkb'),
    url(r'^(?P<type>\d+)/kb_list/$', views.kb_list, name='kb_list'),
    url(r'^(?P<kbid>\d+)/kb_detail/$', views.kb_detail, name='kb_detail'), 
    url(r'^my_kb_list/$', views.my_kb_list, name='my_kb_list'),
    url(r'^all_kb_list/$', views.all_kb_list, name='all_kb_list'),
    url(r'^upload_image/$', views.upload_image, name='upload_image'),
    
    url(r'^del_pic/$', views.del_pic, name='del_pic'),
    url(r'^savekb/$', views.savekb, name='savekb'), # 
    url(r'^(?P<kbid>\d+)/set_kb_top_pic/$', views.set_kb_top_pic, name='set_kb_top_pic'), 
    url(r'^save_kb_top_pic/$', views.save_kb_top_pic, name='save_kb_top_pic'),
    url(r'^(?P<kbid>\d+)/changekb/$', views.changekb, name='changekb'),
    
    url(r'^new_speak_wall_kb/$', views.new_speak_wall_kb, name='new_speak_wall_kb'),
    url(r'^takepart_in/$', views.takepart_in, name='takepart_in'),
    url(r'^(?P<kbid>\d+)/delkb/$', views.delkb, name='delkb'),
    url(r'^(?P<kbid>\d+)/best_kb/$', views.best_kb, name='best_kb'),
    url(r'^(?P<kbid>\d+)/cancel_best_kb/$', views.cancel_best_kb, name='cancel_best_kb'),
    
    url(r'^award_kb/$', views.award_kb, name='award_kb'),
    url(r'^(?P<kbid>\d+)/award_userlist/$', views.award_userlist, name='award_userlist'),  
    url(r'^(?P<kbid>\d+)/active_userlist/$', views.active_userlist, name='active_userlist'), #
    url(r'^collect_kb/$', views.collect_kb, name='collect_kb'),
    url(r'^collect_list/$', views.collect_list, name='collect_list'), #
    
    url(r'^collect_del_kb/$', views.collect_del_kb, name='collect_del_kb'),
    url(r'^(?P<blockid>\d+)/new_product_kb/$', views.new_product_kb, name='new_product_kb'),#
    url(r'^(?P<blockid>\d+)/new_gift_kb/$', views.new_gift_kb, name='new_gift_kb'),## 
    
    
    url(r'^(?P<kbid>\d+)/freegift_userlist/$', views.freegift_userlist, name='freegift_userlist'),
    url(r'^my_freegift/$', views.my_freegift, name='my_freegift'),
    url(r'^my_book/$', views.my_book, name='my_book'),
    url(r'^all_my_kb_list/$', views.all_my_kb_list, name='all_my_kb_list'),
    
    url(r'^(?P<kbid>\d+)/recommend_to_block/$', views.recommend_to_block, name='recommend_to_block'),#
    url(r'^(?P<kbid>\d+)/recommend_to_homepage_slice/$', views.recommend_to_homepage_slice, name='recommend_to_homepage_slice'),
    url(r'^(?P<kbid>\d+)/recommend_to_homepage/$', views.recommend_to_homepage, name='recommend_to_homepage'),
    url(r'^search/$', views.search, name='search'),
    url(r'^good_add/$', views.good_add, name='good_add'),#

    url(r'^(?P<type>\d+)/new_group_kb/$', views.new_group_kb, name='new_group_kb'),
    url(r'^publish_kb/$', views.publish_kb, name="publish_kb"),
    url(r'^confirm_kb/$', views.confirm_kb, name='confirm_kb'),
    url(r'^add_iwant/$', views.add_iwant, name='add_iwant'),
    url(r'^add_iate/$', views.add_iate, name='add_iate'),

    url(r'^(?P<kbid>\d+)/set_kb_property/$', views.set_kb_property, name='set_kb_property'), 
    url(r'^create_magazine/$', views.create_magazine, name='create_magazine'), 
    url(r'^magazine_kb/$', views.magazine_kb, name='magazine_kb'), 
    url(r'^add_kb_magazine/$', views.add_kb_magazine, name='add_kb_magazine'),
    url(r'^del_kb_magazine/$', views.del_kb_magazine, name='del_kb_magazine'),

    url(r'^(?P<magazineid>\d+)/magazine_detail/$', views.magazine_detail, name='magazine_detail'), 

)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
