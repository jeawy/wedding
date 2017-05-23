# -*- coding: utf-8 -*-

from django.shortcuts import render
import getpass 
from administration.models import User, VerifyCode

import pdb
from django.utils import timezone
import datetime
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
import os
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
from datetime import datetime


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

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
from PIL import Image
from kb.models import Article 
"""
3 L
"""
from basedatas.bd_comm import Common
from common.stat import StatComm
 
from comment.models import Comment  


dmb     = DetectMobileBrowser()
comm    = Common()

sys_log = settings.SYS_LOGGING

@csrf_exempt
def add_fresh(request):
    isMobile = dmb.process_request(request)
    if  request.user.is_anonymous():
        return comm.redirect_login_path(isMobile, request)
    result = {}
    
    if request.method == 'POST':
        if 'kbid' in request.POST and 'content' in request.POST:
            kbid    = request.POST['kbid']
            content = request.POST['content']
            
            try:
                kb = Article.objects.get(pk = kbid)
                
                comment = Comment(commenter = request.user, kb = kb, date = timezone.now(), content = content)
                comment.save()
 
                kb.count_reply = kb.comment_set.all().count()
                kb.save()
                '''
                if request.user != kb.author:
                    add_msg(request, kb, content)
                '''
                
                result['status'] = 'OK'
                result['msg'] = '评论成功...'
            except Article.DoesNotExist:
                sys_log.warnging('[Article.DoesNotExist]add fresh comment request parameter error in POST')
            except Article.MultipleobjectReturned:
                sys_log.warnging('[Article.MultipleobjectReturned]add fresh comment request parameter error in POST')
        else:
            sys_log.warnging('add fresh comment request parameter error in POST')
    else:
        sys_log.warnging('add fresh comment request method error')

    return HttpResponse(json.dumps(result), content_type='application/json')
    
@csrf_exempt
def add_replied(request):
    isMobile = dmb.process_request(request)
    if  request.user.is_anonymous():
        return comm.redirect_login_path(isMobile, request)
    result = {}
    
    if request.method == 'POST':
        if 'kbid' in request.POST and 'content' in request.POST and 'currentcommentid' in request.POST:
            kbid             = request.POST['kbid']
            content          = request.POST['content']
            currentcommentid = request.POST['currentcommentid']
 
            try:
                kb = Article.objects.get(pk = kbid)
                try:
                    comment_old = Comment.objects.get(pk = currentcommentid)
                    
                    comment = Comment(commenter = request.user, kb = kb, date = timezone.now(), type =1, content = content, replied_comment=comment_old)
                    comment.save()
 
                    kb.count_reply = kb.comment_set.all().count()
                    kb.save()

                    
                    result['status'] = 'OK'
                    result['msg'] = '评论成功...'
                except Comment.DoesNotExist:
                    sys_log.warnging('Comment.DoesNotExist error')
                    result['status'] = 'ERROR'
                    result['msg'] = '错误1...'
            except Article.DoesNotExist:
                sys_log.warnging('[Article.DoesNotExist]add replied comment request parameter error in POST')
                result['status'] = 'ERROR'
                result['msg'] = '错误2...'
            except Article.MultipleobjectReturned:
                sys_log.warnging('[Article.MultipleobjectReturned]add replied comment request parameter error in POST')
                result['status'] = 'ERROR'
                result['msg'] = '错误3...'
        else:
            sys_log.warnging('add replied comment request parameter error in POST')
            result['status'] = 'ERROR'
            result['msg'] = '错误4...'
    else:
        sys_log.warnging('add replied comment request method error')
        result['status'] = 'ERROR'
        result['msg'] = '错误5...'

    return HttpResponse(json.dumps(result), content_type='application/json')


def add_msg(request, kb, content, type = 1):
    #call msg app to add msg item to DB
    msg_url = reverse('kb:kb_detail', args={ kb.id})
    if len( content ) > 100:
        msgtext = content[:100] + '...'
    else:
        msgtext = content
    urlpic = '' 
    #type = 1 # from comment app
    MsgComm.add(kb.author, msg_url, urlpic, msgtext, type, request.user)

    #to prompt the owner
    kb.author.msg_mark = True
    kb.author.save()
    
def add_comment_silver_award(user, kb):
    """
    award user silver when comment a kb, the upper limit is set in setting file
    """
    #section for sliver 
    reach_top = MoneyComm.reachCommentTopMoney(user) 
    if not reach_top: 
        MoneyComm.awardComment(user, kb)
       
