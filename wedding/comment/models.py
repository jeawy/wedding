# -*- coding: utf-8 -*- 
from django.db import models
from administration.models import User
from kb.models import Article

class Comment( models.Model ):
    """
    the table for comment of public feature 
    """
    commenter     = models.ForeignKey(User, verbose_name = '', related_name='commenter')
    kb            = models.ForeignKey(Article, verbose_name = '帖子', null = True)
    date          = models.DateTimeField(auto_now_add = True)
    content       = models.TextField()
    
    #value = 0,   fresh comment, ex: an user comment some feature.
    #value = 1,   replied commnet, ex: someone replied some comments.
    type          = models.IntegerField( default = 0)
    
    #when type =1, this column will be used to find which comment is replied by this time.
    replied_comment = models.ForeignKey(
        'self', on_delete = models.CASCADE, null = True
    )
    
    class Meta:
        """
        permission management
        """
        permissions = (
            ("forbid_comment", "forbid an User to comment any feature"),
        )
'''      
class CommentReplied(models):
    """
    An user replied some comments, this model describe the relationship between 
    User and Comment  
    """
    #
    user_at     = models.ForeignKey(User, verbose_name = '') 
'''