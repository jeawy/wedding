# -*- coding: utf-8 -*-

import getpass 
from administration.models import User, VerifyCode
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

from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

from basedatas.bd_comm import Common
from comment.models import Comment
from area.models  import Area

from kb.models import Article,Kb_Recommend
from data.models   import DataPlace, CoveredRate
#validate email format
EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
            
dmb     = DetectMobileBrowser()
comm    = Common()
  
def index(request): 
    isMble  = dmb.process_request(request)

    context = {  } 
    user = request.user
        
    next_url = request.GET.get('next');
    kbs = Kb_Recommend.objects.filter(type_homepage_kb = 1).order_by('-date')
    kb_one = Kb_Recommend.objects.filter(type_homepage_slice = 1).order_by('-date')[0]
    week_kbs = Kb_Recommend.objects.filter(type_block = 1)
    provinces = Area.objects.filter(Q(level = 1) | Q(name=u'北京市'))
    total_city =  Area.objects.filter(level = 2).count()
    total_county =  Area.objects.filter(level = 3).count()
    context ={
        'kbs'         : kbs,
        'week_kbs'    : week_kbs,
        'rootmedia'   : settings.MEDIA_URL,
        'provinces'   : provinces,
        'total_city'     : total_city,
        'total_county'   : total_county,
        'page_title'     : u'分享美食',
        'kb_one'         : kb_one,
    }
    provinces = DataPlace.objects.filter(Q(area__level=1) | Q(area__name=u'北京市'))
    result_provinces=[]
    for province in provinces: 
        result_provinces.append(province.area.short_name)
        
    context['result_provinces'] = result_provinces

    # 
    cr = CoveredRate.objects.all().latest('id')
    context['cr'] = cr
    context['province_num'] = len(result_provinces)
    if next_url: 
            return redirect(next_url)
    else:  
        if isMble:
            return render(request, 'lechi/m_hostpage.html', context)
        else:
            return render(request, 'lechi/hostpage.html', context)
  
def contact_us(request):
    
    isMble  = dmb.process_request(request)  
    content={
        'page_title':u'关于我们'
    }
    if isMble:
        return render(request, 'help/m_contact-us.html', content)
    else:
        return render(request, 'help/contact-us.html', content)
    
    
def user_register(request): 
    dmb     = DetectMobileBrowser()
    isMble  = dmb.process_request(request)
    
    content = {'page':'user_register',
	'page_title':'注册为新会员'} 
    print isMble
    if isMble:
        return render(request, 'basedatas/m_user_register.html', content)
    else:
        return render(request, 'basedatas/user_register.html', content)
        
def find_password(request): 
    isMble  = dmb.process_request(request) 
    content = {'page':'find_password',
	'page_title':'找回密码'}
    if isMble:
        return render(request, 'basedatas/m_user_register.html', content)
    else:
        return render(request, 'basedatas/user_register.html', content)
 
@csrf_exempt
def reset_password(request):
    result = {}
    if request.method == 'POST':
            if 'email' in request.POST and 'verifycode' in request.POST and 'pwd' in request.POST:
                email           = request.POST["email"]
                verifycode      = request.POST["verifycode"]
                pwd             = request.POST["pwd"]
                try:
                    verify_code = VerifyCode.objects.get(email__exact = email, code=verifycode, type ='1')
                    try:
                        user    = User.objects.get(email = email)
           
                        user.set_password(pwd)
                        user.save()
                        verify_code.delete()
                        
                        #send email
                        email_insance = EmailEx()
                        Subject = '吃典密码已重置' 
                        content = '您好, 您在吃典中的密码已重置成功. <br />若不是您本人操作请立即登录重新修改...'
                        try:
                            email_insance.send_text_email(Subject, content, email)
                            result['status']  = 'OK'
                            result['msg'] = '密码重置成功...'
                            return HttpResponse(json.dumps(result), content_type='application/json')
                        except   Exception, e: 
                            result['status']  = 'ERROR'
                            result['err_msg'] = '发送邮件的过程中发生错误： '+ e
                            return HttpResponse(json.dumps(result), content_type='application/json')
                    except User.DoesNotExist:
                        result['status']  = 'ERROR'
                        result['err_msg'] = '您输入的邮箱用户不存在， 请重试... !'
                        return HttpResponse(json.dumps(result), content_type='application/json')
                    
                except VerifyCode.DoesNotExist:
                    result['status']  = 'ERROR'
                    result['err_msg'] = '验证码与邮箱不匹配, 请检查邮件和验证码... !'
                    return HttpResponse(json.dumps(result), content_type='application/json')
            else:
                result['status']  = 'ERROR'
                result['err_msg'] = '非法参数， 你在干什么 !'
                return HttpResponse(json.dumps(result), content_type='application/json')   
    else:
        result['status']  = 'ERROR'
        result['err_msg'] = '非法参数， 你在干什么 !'
        return HttpResponse(json.dumps(result), content_type='application/json') 
def send_email(subject, content, receiver):
    email_insance = EmailEx()
    print 'Thread for sending email'
    #get verify code
    try:
        email_insance.send_text_email(subject, content, receiver)
    except   Exception, e:
        print '发送邮件的过程中发生错误： '+ e
    
@csrf_exempt
def save_user(request):
    
    result={} 
    if request.method == 'POST':
        if 'email' in request.POST and 'verifycode' in request.POST \
              and 'name' in request.POST and  'pwd_1' in request.POST \
                and  'pwd_2' in request.POST:

            user_email  = request.POST["email"].strip()
            verifycode  = request.POST["verifycode"].strip()
            name        = request.POST["name"].strip()
            
            pwd_1       = request.POST["pwd_1"].strip()
            pwd_2       = request.POST["pwd_2"].strip()
                
            #validate email format
            EMAIL_REGEX = re.compile(r'[^@]+@[^@]+\.[^@]+')
            if not EMAIL_REGEX.match(user_email):
                result['status']  = '0'
                result['err_msg'] = '邮箱格式不正确 !'
                return HttpResponse(json.dumps(result), content_type = 'application/json')
                
                
            if pwd_1 != pwd_2:
                result['status']  = '1'
                result['err_msg'] = '您两次输入的密码不一致， 请重新输入 。 '
                return HttpResponse(json.dumps(result), content_type = 'application/json')
 
            if len(pwd_1) < 6:
                result['status']  = '2'
                result['err_msg'] = '密码长度不少于6位...'
                return HttpResponse(json.dumps(result), content_type = 'application/json')
                  
            try:
                obj = User.objects.get(email__exact=user_email)
                result['status']  = '3'
                result['err_msg'] = '邮箱已经注册过了你是不是把密码忘了 ? '
                return HttpResponse(json.dumps(result), content_type = 'application/json')
            except User.DoesNotExist:
                try:
                    verifycode_instance = VerifyCode.objects.get(email__exact = user_email)
                    if verifycode_instance.code == verifycode:
                        try:
                            user = User(name= name, email = user_email, 
                                        date=timezone.now(), password=pwd_1, is_active=True)
                            
                            user.set_password(pwd_1)   
                            user.save()
                            verifycode_instance.delete()
                            result['status']  = '4'
                            result['suc_msg'] = '注册成功， 你可以登录了， 开始使用吧 !'
                                                  
                            Subject = u'New user in 吃典'
                            email_content = 'New user: '+ user_email
                            
			    t_send_email =  threading.Thread(target=send_email, args=[Subject, email_content, settings.SUPPORTOR_EMAIL])
			    t_send_email.start()
			    
                            return HttpResponse(json.dumps(result), content_type = 'application/json') 
                        except e:
                            result['status']  = '5'
                            result['err_msg'] = '保存用户失败! ERROR: ' + e
                            return HttpResponse(json.dumps(result), content_type = 'application/json') 
                    else:
                        result['status']  = '6'
                        result['err_msg'] = '验证码错误， 请重新查看您的验证码!'
                        return HttpResponse(json.dumps(result), content_type = 'application/json') 
                      
                except verifycode.DoesNotExist:
                   
                    result['status']  = '7'
                    result['err_msg'] = '数据库发送错误， 出现重复的邮箱!'
                    return HttpResponse(json.dumps(result), content_type = 'application/json') 
        else:
            result['status']  = '8'
            result['err_msg'] = '参数错误， 非法的输入 !'
            return HttpResponse(json.dumps(result), content_type = 'application/json') 
            
@csrf_exempt
def get_email_verify_code(request):
    result={} 
    if request.method == 'POST':
        if 'email' in request.POST:
            email       = request.POST["email"]
            if not EMAIL_REGEX.match(email):
                result['status']  = '1'
                result['err_msg'] = '电子邮件格式不正确!'
            else: 
                try:
                    obj = User.objects.get(email__exact=email)
                    result['status']  = '2'
                    result['err_msg'] = '邮箱已经注册过,你可以找回密码'
                except User.DoesNotExist: 
                    email_insance = EmailEx()
                    #get verify code
                    code    = ''.join(random.choice(string.lowercase + string.digits) for i in range(5))
                    Subject = u'吃典 注册邮箱验证码' 
                    content = u'您好， 欢迎您注册吃典， 欢迎加入我们， 您的邮箱验证码是：  ' + code 
                    try:
                        email_insance.send_text_email(Subject, content, email)
                        try:
                            verify_code = VerifyCode.objects.get(email__exact = email, type ='0')
                            verify_code.code = code
                            verify_code.save()
                        except VerifyCode.DoesNotExist:
                            verify_code = VerifyCode(email=email, code=code, type ='0')
                            verify_code.save()
                            
                        result['status']  = '3'
                        result['err_msg'] = '验证码已发至您的邮箱中， 请到邮箱中查看您的验证码!'    
                        
                    except   Exception, e:
                        result['status']  = '4'
                        result['err_msg'] = '发送邮件的过程中发生错误： '+ e
        else:
            result['status']  = '5'
            result['err_msg'] = '非法参数， 你在干什么 !'
            
    else:
         result['status']  = '5'
         result['err_msg'] = '非法参数， 你在干什么 !'
        
    return HttpResponse(json.dumps(result), content_type = 'application/json')


@csrf_exempt
def get_reset_pwd_verify_code(request):
    
                        
    result = {}
    if request.method == 'POST':
        if 'email' in request.POST:
            email       = request.POST["email"]
            
            if not EMAIL_REGEX.match(email):
                result['status']  = 'ERROR'
                result['err_msg'] = '亲， 电子邮件格式不正确哦 !'
                return HttpResponse(json.dumps(result), content_type='application/json')
            else: 
                try:
                    user    = User.objects.get(email = email)
                except User.DoesNotExist:
                    result['status']  = 'ERROR'
                    result['err_msg'] = '用户不存在,该用户尚未注册... !'
                    return HttpResponse(json.dumps(result), content_type='application/json')  
                        
                email_insance = EmailEx()
                #get verify code
                code    = ''.join(random.choice(string.lowercase + string.digits) for i in range(4))
                Subject = '吃典重置密码验证码' 
                content = ('您好， 您正在重置您在吃典的密码，输入正确的验证码后，即可修改您的密码。  验证码是：  ' 
                           + code + ' <br />感谢您使用吃典。')
                try:
                    email_insance.send_text_email(Subject, content, email)
                except   Exception, e: 
                    result['status']  = 'ERROR'
                    result['err_msg'] = '发送邮件的过程中发生错误： '+ e
                    return HttpResponse(json.dumps(result), content_type='application/json')
                try:
                    verify_code = VerifyCode.objects.get(email__exact = email, type ='1')
                    verify_code.code = code
                    verify_code.save()
                except VerifyCode.DoesNotExist:
                    verify_code = VerifyCode(email=email, code=code, type ='1')
                    verify_code.save()
                result['status']  = 'OK'
                result['msg'] = '验证码已发至您的邮箱中， 请到邮箱中查看您的验证码 !'
                return HttpResponse(json.dumps(result), content_type='application/json')    
                
                    
        else:
            result['status']  = 'ERROR'
            result['err_msg'] = '非法参数， 你在干什么 !'
            return HttpResponse(json.dumps(result), content_type='application/json')  
    else:
        result['status']  = 'ERROR'
        result['err_msg'] = '非法参数， 你在干什么 !'
        return HttpResponse(json.dumps(result), content_type='application/json')               
@csrf_exempt
def validate_username(request):
    if request.method == 'POST':

        username    = request.POST["username"]
        try:
            User.objects.get(username = username)
            return HttpResponse('nThe username is exist, please input another one !')
        except:
            return HttpResponse('yAvailble !')
@csrf_exempt
def validate_uniqueness_email(request):
    if request.method == 'POST':
        if 'email' in request.POST :
            email    = request.POST["email"]
            users    = User.objects.filter(email = email)
            if users.count() > 0:#The email is exist
               return HttpResponse('nThe email is exist, please input another one !')
        else:
            return HttpResponse('nCannot get the email address !')   
    else:
        return HttpResponse('nMethdod error !')   
 