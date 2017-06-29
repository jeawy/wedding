# -*- coding: utf-8 -*-
from django.db import models

class Todo_list(models.Model):
    
    STATUS = (
        ('0', u'男方'),
        ('1', u'女方'),
    )
    COME_OR_NOT = (
        ('0', u'出席'),
        ('1', u'不出席'),
    )
    date         = models.DateTimeField('创建日期', auto_now_add=True) 
    name         = models.CharField( max_length=1000,verbose_name='姓名') 
    phone        = models.CharField( max_length=1000,verbose_name='电话',default='')
    address      = models.TextField('地址及留言',default='')  
    whichside    = models.CharField(choices=STATUS, max_length=10, default='0') 
    come    = models.CharField(choices=COME_OR_NOT, max_length=10, default='0') 
    class Meta:
        ordering = ['-date']
    