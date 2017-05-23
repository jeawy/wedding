from django.shortcuts import render
 
from mobile.detectmobilebrowsermiddleware import DetectMobileBrowser

from basedatas.bd_comm import Common
from common.stat import StatComm
  
from msg.models import Msg 
import pdb
   
dmb     = DetectMobileBrowser()
comm    = Common()
    
        
def add(request):
    pass
    
def delete(request):
    pass

def index(request):
    """
    get all msg belong to current user
    """
    StatComm.count_page_traffic(request)
    is_Mobile = dmb.process_request(request)
    if  request.user.is_anonymous():
            return comm.redirect_login_path(is_Mobile, request)
    
    msg_list = Msg.objects.filter(owner = request.user).order_by('-date')
    request.user.msg_mark = False;
    request.user.save()
    
    context = {'msg_list':msg_list}
    if is_Mobile:
          return render(request, 'msg/m_index.html', context )
    else:                
          return render(request, 'msg/m_index.html', context )
                
    