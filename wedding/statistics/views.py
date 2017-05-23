from django.shortcuts import render
from django.shortcuts import redirect
import pdb
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from django.db import connection
from django.db.models import Sum, Count




from django.conf import settings
from django.contrib.auth.models import User


def dashboard(request):
    if  request.user.is_anonymous():
        return redirect(settings.APP_WEB_LOGIN_URL)
    
   
    context = {
    }
    
    return render(request, 'statistics/index.html', context)
