# -*- coding: utf-8 -*-
from django.db import models

from administration.models import User 
from kb.models import Article
from django.utils import timezone

     
# stay praise for every kb
class G_kb(models.Model):
     owner = models.ForeignKey(User)
     app   = models.ForeignKey(Article)

	
