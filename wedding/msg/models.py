from django.db import models
from administration.models import User


class Msg(models.Model):
    owner      = models.ForeignKey(User)
    #the destination url
    url        = models.CharField(max_length = 2048, default='/')
    #the picture link for message
    piclink    = models.CharField(max_length = 2048, null=True)
    #the short message
    msgtext    = models.CharField(max_length = 2048, default='new msg')
    #the visibility to the owner, 
    #the default value is True, the owner can see this msg in his/her unhandled list
    #if the owner has handled the msg, visibility will be set to False, but can be find in msg history list 
    visibility = models.BooleanField(default = True)
    
    date       = models.DateTimeField(auto_now_add = True)
    
    #0 stand for good app msg
    #1 stand for comment app msg
    #more
    type       = models.IntegerField(default = 0)
