# -*- coding: utf-8 -*- 

 
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render 
import pdb 
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone 
from django.core.urlresolvers import reverse

'''
layer 3 start
'''
from .models import Todo_list
from .form import Todo_listForm
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser
from basedatas.bd_comm import Common
from django.contrib.auth.decorators import login_required
'''
layer 3 end
'''


dmb     = DetectMobileBrowser()
comm    = Common()


'''
TODO list section  START
'''
@login_required() 
def todolist(request):
    '''
    list all TODO
    '''
    isMobile = dmb.process_request(request)
 
        
    has_perm = request.user.has_perm('task.manage_todolist')
     
    todo_ls = Todo_list.objects.all().order_by('-date')
     
        
    context = {'has_perm': has_perm,
               'todo_ls' : todo_ls  }
    if isMobile:
        return render(request, 'task/m_todolist.html', context)
    else:
        return render(request, 'task/todolist.html', context)


'''
TODO list section  END
'''

def delitem(request, pk): 
    todo = Todo_list.objects.get(pk = pk)
    todo.delete() 
    return HttpResponseRedirect(reverse('task:todolist'))