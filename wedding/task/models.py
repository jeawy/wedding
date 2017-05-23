# -*- coding: utf-8 -*-
from django.db import models
from administration.models import User

class Todo_list(models.Model):
    STATUS = (
        ('0', u'未开始'),
        ('1', u'正在进行'),
        ('2', u'已完成'),
    )
    date             = models.DateTimeField('创建日期')
    publisher        = models.ForeignKey(User, verbose_name='发布者', null=True) 
    description      = models.TextField('任务描述')  
    finisher         = models.ForeignKey(User, related_name='finisher', verbose_name='finisher', null=True) 
    finish_date      = models.DateTimeField('任务完成的日期', null=True)
    title            = models.CharField( max_length=1000,verbose_name='待办任务', default='任务名称') 
    #'0' stand for new published
    #'1' in process
    #'2' finished and in maintainance
    status           = models.CharField(choices=STATUS, max_length=10, default='0') 
    class Meta:
        permissions = (
            ("manage_todolist", "Can manage TODO list"), 
        )
        ordering = ['-date', 'status']


class Todo_engineer(models.Model):
    engineer         = models.ForeignKey(User, verbose_name='工程师') 
    todo_id          = models.ForeignKey(Todo_list)
     
    #the date to reject or accept this task.
    date             = models.DateTimeField('日期')
    
    #'0' stand for reject
    #'1' stand for accept
    status           = models.CharField(max_length=10, default='1')
    
    #if the engineer reject this task, he\she should provide the reason.  
    reason           = models.TextField('拒绝的原因')
    
class Todo_comments(models.Model):
    user             = models.ForeignKey(User, verbose_name='工程师') 
    todo          = models.ForeignKey(Todo_list)
     
    #the date to reject or accept this task.
    date             = models.DateTimeField('日期', auto_now_add=True)
    
    comments        = models.TextField('评论内容')
    
    