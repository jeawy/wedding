# -*- coding: utf-8 -*-

import getpass  
import pdb
from django.utils import timezone
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render


from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import random
import string
from django.template import RequestContext, loader
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import threading

import smtplib
from email import encoders
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart  
from email.MIMEText import MIMEText
from basedatas.e_mail import EmailEx

from django.conf import settings
from django.db.models import Q
import re
from task.models import Todo_list
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

from basedatas.bd_comm import Common
 
 
#validate email format
EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
            
dmb     = DetectMobileBrowser()
 
@csrf_exempt
def index(request): 
    isMble  = dmb.process_request(request)

    context = {  } 
    user = request.user
    if request.method == 'POST': 
        name = request.POST['name']
        msg = request.POST['msg']
        phone = request.POST['phone']
        come = request.POST['come']
        todo = Todo_list.objects.create(name=name, phone=phone,address=msg ,come=come)
        todo.save()
        return HttpResponse('ok');
    next_url = ''
    if next_url: 
            return redirect(next_url)
    else:  
        if isMble:
            return render(request, 'lechi/m_hostpage.html', context)
        else:
            return render(request, 'lechi/m_hostpage.html', context)
   