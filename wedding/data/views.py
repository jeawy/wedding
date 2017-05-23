# -*- coding:utf8 -*-
from __future__ import division

import json
import pdb 

from django.db.models import Q
from django.shortcuts import render
from django.http      import HttpResponse
from django.conf      import settings
from kb.models import FoodLocation
from .models   import DataPlace, CoveredRate
from area.models import Area
from kb.models   import Article, Kb_Recommend, Kb_Magazine,Magazine
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

dmb     = DetectMobileBrowser()

def update_data_place(request):
    """统计哪些地方已经有了美食"""
    food_areas = FoodLocation.objects.all()
    provinces = DataPlace.objects.all()
    areas = []
    for f_area in food_areas:
        mark     = False # 默认情况下，当前地址并不在列表中
        tmp_area = f_area.area
        
        for province in provinces: 
            if tmp_area.id == province.area.id: 
                mark = True #表示已经存在
                break
        if mark == False:
            areas.append(tmp_area)
            """
            p = DataPlace.objects.create(area = tmp_area)
            p.save()
            # 更新data province列表
            provinces = DataPlace.objects.all()
            """
    
    for area in areas:
        p = DataPlace.objects.create(area = area, num=1)
        p.save()
        if area.level == 3:
            # 县级：同时要加入其上一级市级以及省级
            parent = Area.objects.get(pk = area.parent_id)

            dps = DataPlace.objects.filter(area = parent)
            if len(dps ) == 0:
                area_parent,created  = DataPlace.objects.get_or_create(area = parent, num=1)
                area_parent.save()

            grandpa = Area.objects.get(pk = parent.parent_id) 
            dps = DataPlace.objects.filter(area = grandpa)
            if len(dps ) == 0:
                area_grandpa,created  = DataPlace.objects.get_or_create(area = grandpa, num=1)
                area_grandpa.save()
        elif area.level == 2 and area.name != u'北京市':
            # 市级：同时要加入其上一级市级以及省级
            parent = Area.objects.get(pk = area.parent_id)

            dps = DataPlace.objects.filter(area = parent)
            if len(dps ) == 0:
                area_parent,created  = DataPlace.objects.get_or_create(area = parent, num=1)
                area_parent.save() 
                
    provinces = DataPlace.objects.all()
    result=[]
    for province in provinces: 
        result.append(province.area.short_name)     
    return render(request, 'data/records.html' , {'result': result})


def update_data_place_rate(request):
    """统计已经收集的省级、市级、县级数量的百分比"""
    areas = Area.objects.filter(level__in = [1,2,3])
    provinces_count = areas.filter(level = 1).count()
    city_count      = areas.filter(level = 2).count()
    county_count    = areas.filter(level = 3).count()
    
    update_data_place(request)

    # 已经收集的省级数量
    province_ready_count = DataPlace.objects.filter(area__level = 1).count()
    city_ready_count     = DataPlace.objects.filter(area__level = 2).count()
    county_ready_count   = DataPlace.objects.filter(area__level = 3).count()

    province_rate = province_ready_count/provinces_count
    city_rate     = city_ready_count/city_count
    county_rate   = county_ready_count/county_count
    
    c_r = CoveredRate.objects.create(province_rate = province_rate,
                               city_rate     = city_rate,
                               county_rate   = county_rate,
                               province_count = province_ready_count,
                               city_count = city_ready_count,
                               county_count = county_ready_count, )
    c_r.save()



    content={
        'provinces_count' : province_ready_count,
        'city' : city_ready_count,
        'county' : county_ready_count,
    }
    return render(request, 'data/records.1.html' , content)

def latest_kb(request):
    """
    最新分享
    """
    kbs = Kb_Recommend.objects.filter(type_homepage_kb = 1).order_by('-kb__date')[:60]
    isMobile        = dmb.process_request(request)
    content = {
        'kbs'  : kbs,
        'rootmedia': settings.MEDIA_URL, 
        'page_title' : u'最新分享',
    }
    if isMobile:
        return render(request, 'data/m_kblist.html' , content)
    else:
        return render(request, 'data/kblist.html' , content)

def week_recommend_kb(request):
    """
    本期推荐
    """
    isMobile        = dmb.process_request(request)

    kbs = Kb_Recommend.objects.filter(type_block = 1).order_by('-kb__date')[:60]
    
    magazines = Magazine.objects.all()
    current_magazineid  = 0 
    page_title =  u'本期推荐'
    if 'magazineid' in request.GET:
        magazineid = request.GET['magazineid']
        current_magazine = Magazine.objects.get(pk = magazineid)
        page_title  = current_magazine.title
        current_magazineid = current_magazine.id
        kbs         = Kb_Magazine.objects.filter(magazine = current_magazine)
    
    content = {
        'kbs'  : kbs,
        'rootmedia': settings.MEDIA_URL,
        'page_title' : page_title,
        'magazines'  : magazines, 
        'current_magazineid' :current_magazineid,
    }
    if isMobile:
        return render(request, 'data/m_kblist.html' , content)
    else:
        return render(request, 'data/kblist.html' , content)

def map(request ):
    isMobile        = dmb.process_request(request)
    total_city =  Area.objects.filter(level = 2).count()
    total_county =  Area.objects.filter(level = 3).count()
    provinces = DataPlace.objects.filter(Q(area__level=1) | Q(area__name=u'北京市'))
    result_provinces=[]
    for province in provinces: 
        result_provinces.append(province.area.short_name)
        
    cr = CoveredRate.objects.all().latest('id')

    content = {
        'result_provinces':result_provinces,
        'total_city'     : total_city,
        'total_county'   : total_county,
        'page_title' : u'数据统计',
        'cr': cr,
        'province_num':len(result_provinces),
    }
    
    if isMobile:
        return render(request, 'data/m_map.html', content)
    else:
        return render(request, 'data/map.html', content)