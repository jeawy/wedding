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
 

 
