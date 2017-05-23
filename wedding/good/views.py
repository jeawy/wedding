# -*- coding: utf-8 -*- 

from .models import *
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.core.urlresolvers import reverse
import pdb 
import json


from django.views.decorators.csrf import csrf_exempt
from basedatas.models import Day_words
from good.models import G_daywords
from msg.msg_comm import MsgComm

@csrf_exempt
def delele(request):
    result = good_result(request, 0)
    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def  add(request): 
     result = good_result(request, 1)
     return HttpResponse(json.dumps(result), content_type='application/json')

'''
mark = 1. add good
mark = 0  del good
'''
def good_result(request, mark):
    
    result = {}
    
    if  request.user.is_anonymous():
        result['status'] = '1'#need to login
        result['msg'] = 'please login first'
        return result
         
    else:  
        if request.method == 'POST':
            if 'day_words_id' in request.POST :
                day_words_id = request.POST.get('day_words_id')
            else:
                result['status'] = '2'# exception
                result['msg'] = 'ERROR CODE 2...'
                return result
        else:
                result['status'] = '3'# exception
                result['msg'] = 'ERROR CODE 3...'
                return result
        try:
            try: 
                
                Day_words_instance = Day_words.objects.get(pk = day_words_id)
                 
                if mark: 
                    Day_words_instance.good_count = Day_words_instance.good_count + 1
                    #mark there is new msg 
                    Day_words_instance.user.msg_mark = True
                    Day_words_instance.user.save() 
                    
                    #start to add new msg to msg app
                    #call msg app to add msg item to DB
                    msg_url = reverse('base:go_comment', args={ Day_words_instance.id}) 
                    msgtext = '您收到一个喜欢...'
                    urlpic = '' 
                    type = 0 # from good app
                    MsgComm.add(Day_words_instance.user, msg_url, urlpic, msgtext, type)
                    #call msg app to add msg item to DB ---end
                else: 
                    Day_words_instance.good_count = Day_words_instance.good_count - 1
                
                Day_words_instance.save()
            except Day_words.DoesNotExist:
                result['status'] = '4'# exception
                result['msg'] = 'ERROR CODE 4...'
                return result
            try:  
                if mark:
                    good_day_words_instance    = G_daywords.objects.create(app = Day_words_instance, owner=request.user) 
                    good_day_words_instance.save()
                else:
                    good_day_words_instance    = G_daywords.objects.get(app = Day_words_instance, owner=request.user)
                    good_day_words_instance.delete()
                    
                
            except G_daywords.DoesNotExist: 
                pass
            except G_daywords.MultipleObjectsReturned: 
                # delete all records   
                good_day_words_ls    = G_daywords.objects.filter(app = Day_words_instance, owner=request.user)
                for good_day_words in good_day_words_ls:
                    good_day_words.delete()
                
            result['status'] = '0' 
            result['msg'] = 'SUCCESS...'
            return result
        except:
            result['status'] = '6'# exception
            result['msg'] = 'ERROR CODE 6...'
            return result