# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
import shutil
from django.contrib.admin import AdminSite
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
import pdb

"""
layer 2 start
"""
from django.contrib.auth import logout

"""
layer 2 end
"""
 
from basedatas.bd_comm import Common

dmb     = DetectMobileBrowser()
comm    = Common()
 
@csrf_exempt    
def login(request):
    isMble  = dmb.process_request(request)

    if  'password' in request.POST:
            auth.logout(request)
            username       = 'admin'
            password      = request.POST['password']  
            user = auth.authenticate(username =username, password=password)
         
            context ={}
            next_url = '/'
            if user: 
                request.user = user
                auth.login(request, user) 
		 
                return redirect(next_url) 
            else:  
                msg = '密码错误...' 
                context = {'error':msg} 
                if isMble: 
		    return render(request, 'm_login.html', context)
		else:  
		    return render(request, 'login.html', context)
		    
    else: 
        email = request.POST.get('email')
        context = {'error':''} 
        if isMble:
            return render(request, 'm_login.html', context)
        else:
            return render(request, 'login.html', context)

 
