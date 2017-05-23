# -*- coding:utf8 -*-
import pdb
import itertools 

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
from area.models import Area
from kb.models import Article, FoodLocation
from .models   import Words
from basedatas.bd_comm import Common


dmb     = DetectMobileBrowser()
comm    = Common()

def inplace(request ):
    kwargs  = {}
    content = {}
    isMobile = dmb.process_request(request)
    if 'homepage_province' in request.GET:
        homepage_province = int(request.GET['homepage_province'].strip())
        # 搜索某地的美食
        if homepage_province  -1:
            placeid = homepage_province

    if 'homepage_city' in request.GET: 
        homepage_city     = int(request.GET['homepage_city'].strip())
         
        if homepage_city > -1:
            placeid = homepage_city
        
    if  'homepage_county' in request.GET:  
        homepage_county   = int(request.GET['homepage_county'].strip()) 
        if homepage_county > -1:
            placeid = homepage_county

    if 'placeid' in request.GET :
        placeid  = int(request.GET['placeid'].strip())
    
        # 用户搜索的时候没有输入关键字，此时应该给出一些默认的推荐的美食
        # return  render(request, 'search/inplace.html', content)
 
    content = foods_inplace(placeid, request)

    provinces = Area.objects.filter(level = 1)
    content['provinces'] = provinces
    content['rootmedia'] = settings.MEDIA_URL
    content['page_title'] = u'搜索美食'
    if isMobile:
        return render(request, 'search/m_inplace.html', content)
    else:
        return render(request, 'search/inplace.html', content)
     
 
def foods_inplace(placeid, request):
    """
    根据地名搜索各地的美食，
    如果搜索的是县级，且县级没有搜到，则搜索上一级的市级
    如果搜索的是市级，且市级没有搜到，则搜索上一级的省级
    """
    content = {}
    try:
        area = Area.objects.get(pk = placeid)

        comm = Common()
        ip = comm.get_client_ip(request)
        if request.user.is_anonymous():
             words = Words.objects.create(area=area,ip=ip)
        else:
             words = Words.objects.create(area=area,ip=ip, user= request.user)
        
        words.save()

        content['area'] = area
        if area.level == 2: # 市：搜索该市的所有美食，包括县。
            foodslocation = FoodLocation.objects.filter(Q(area = area) | Q(area__parent_id=area.id))
        elif area.level == 3:
            foodslocation = FoodLocation.objects.filter(area = area) 
        elif area.level == 1:
            cities_under =  Area.objects.filter(parent_id = area.id)
            foodslocation = []
            for city_under in cities_under:
                foodslocation_item = FoodLocation.objects.filter(Q(area = city_under) | Q(area__parent_id=city_under.id))
                if len(foodslocation_item) > 0:
                    foodslocation += foodslocation_item 
 
        if area.level == 2 or area.level == 1: 
            kbids = []
            new_foodslocation = []
            for foodlocation in foodslocation:
                if foodlocation.kb.id not in kbids:
                    kbids.append(foodlocation.kb.id )
                    new_foodslocation.append(foodlocation)
            foodslocation = new_foodslocation

        content['foodslocation'] = foodslocation

        if len(foodslocation )  == 0:
            # 在当地没有搜索出来记录，应该提示给用户，并搜索上一级地方的美食
            # 如县级没有搜出来，就搜市级； 市级没有搜出来，就搜省级
            content['status'] = 1 # 1 代表原来的搜索条件没有搜到记录
            
        elif len(foodslocation) < 13:
            # 搜索出来不到13个记录，为了丰富内容，还应该继续搜索推荐内容
            content['status'] = 2 # 2 代表搜到了记录，但是但是记录比较少

        if area.level == 3: # 当前为县级
            # 查找了市级的记录
            city_locations = FoodLocation.objects.filter(area__id = area.parent_id)
            
            # 查找了省级级的记录
            city = Area.objects.get(pk = area.parent_id)     # 市
            province = Area.objects.get(pk = city.parent_id) # 省
            province_locations = FoodLocation.objects.filter(area__id = city.parent_id)
            
            cities   = Area.objects.filter(parent_id = city.parent_id)     # 同级市
            counties = Area.objects.filter(parent_id = area.parent_id)     # 同级县

            content['city']               = city
            content['cities']             = cities
            content['counties']           = counties
            content['province']           = province
            content['city_locations']     = city_locations
            content['province_locations'] = province_locations
        elif area.level == 2: # 当前为市级
            # 查找了市级的记录
            province = Area.objects.get(pk = area.parent_id)   # 省
            # province_locations = FoodLocation.objects.filter(area__id = province.id)
            cities_under =  Area.objects.filter(parent_id = area.parent_id)
            province_locations = []
            for city_under in cities_under:
                foodslocation_item = FoodLocation.objects.filter(Q(area = city_under) | Q(area__parent_id=city_under.id))
                if len(foodslocation_item) > 0:
                    province_locations += foodslocation_item 
            
            kbids = []
            new_foodslocation = []
            for foodlocation in province_locations:
                if foodlocation.kb.id not in kbids:
                    kbids.append(foodlocation.kb.id )
                    new_foodslocation.append(foodlocation)
            
            province_locations = new_foodslocation
            cities = Area.objects.filter(parent_id = area.parent_id)     # 同级县
            content['city']               = area
            content['cities']             = cities
            content['province']           = province
            content['province_locations'] = province_locations
        else: # 省级
            cities = Area.objects.filter(parent_id = area.id)     # 该省级所有的市
            content['province']           = area
            content['cities']             = cities
        return content

    except Area.DoesNotExist:
        raise Http404


def search_all(request ):
    # 根据关键词搜索地方美食
    content = {}
    isMobile = dmb.process_request(request)
    keywords = ''
    if 'keywords' in request.GET:
        keywords = request.GET['keywords'].strip()
        content['keywords'] = keywords

        comm = Common()
        ip = comm.get_client_ip(request)
        
        if request.user.is_anonymous():
                words = Words.objects.create(keywords=keywords,ip=ip)
        else:
                words = Words.objects.create(keywords=keywords,ip=ip, user= request.user)
    
        words.save()
    if keywords:
        kbs = Article.objects.filter(title__contains = keywords) 
        #kbs = Article.objects.all()
        kbs.extra(
                select={'strength':'count_read+count_good+count_reply+count_confirm'},
                order_by=('strength')
                )
    else:
        kbs = ''
    content['kbs'] = kbs
    content['rootmedia'] = settings.MEDIA_URL
    provinces            = Area.objects.filter(level = 1)
    content['provinces'] = provinces
    content['page_title'] = u'搜索美食'
    if isMobile:
        return render(request, 'search/m_search.html', content)
    else:
        return render(request, 'search/search.html', content)
     

def test_search(request):
    return render(request, 'search/search.1.html', {})



def search_records(request):
    """
    查看用户的搜索记录
    """
    isMobile = dmb.process_request(request)
    user = request.user
    if user.is_anonymous():
        return comm.redirect_login_path(isMobile, request)
    
    if not user.is_superuser:
        return HttpResponse('not u')
    
    words = Words.objects.all()
    content = {
        'words' :words,
        'page_title': u'搜索记录'
    }
    if isMobile:
        return render(request, 'search/m_searchrecords.html', content)
    else:
        return render(request, 'search/searchrecords.html', content)