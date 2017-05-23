from django.apps import AppConfig
from django.utils import timezone
from .models import To_do_list
import pdb
class To_do_list_cls():
    def add(self,sender, receivers, url, decription, type, app_id, app_type,
            visibility):
        if app_type == '0':
            to_do_list_instance= To_do_list(createDate=timezone.now(), sender=sender,       
                            receivers = receivers, url=url,description= decription,
                            type=type, app_fix=app_id,app_type=app_type,
                            visibility=visibility,Status='0')
        else:
            to_do_list_instance= To_do_list(createDate=timezone.now(), sender=sender,       
                            receivers = receivers, url=url,description= decription,
                            type=type, app_problem=app_id,app_type=app_type,
                            visibility=visibility,Status='0')
            
        to_do_list_instance.save()

    def addForFix(self,sender, receivers, type, app,visibility='1'):
        to_do_list_instance= To_do_list(createDate=timezone.now(), sender=sender,       
                            receivers = receivers, type=type, app_fix=app,
                            app_type='0',  visibility=visibility,Status='0')
        to_do_list_instance.save()
        
    def addForProblem(self,sender, receivers, type, app, visibility='1'):
        to_do_list_instance= To_do_list(createDate=timezone.now(), sender=sender,       
                            receivers = receivers, type=type, app_problem=app,
                            app_type='1',  visibility=visibility,Status='0')
        to_do_list_instance.save()
        
    def update(self,id, sender, operator, ip, Status):
            to_do_list_instance= To_do_list.objects.get(id=id)
            to_do_list_instance.finishDate  = timezone.now()
            to_do_list_instance.operator    = operator
            to_do_list_instance.ip          = ip
            to_do_list_instance.Status      = Status
            to_do_list_instance.save()
    
    def delete(self,id):
            to_do_list_instance= To_do_list.objects.get(id=id)
            to_do_list_instance.finishDate  = timezone.now()
            to_do_list_instance.operator    = operator
            to_do_list_instance.ip          = ip
            # '-1' stand for this item has been deleted.
            to_do_list_instance.Status      = '-1'
            to_do_list_instance.save()
    def delete_Fix(self,app,ip,operator):
            to_do_list_instances= To_do_list.objects.filter(app_fix__exact=app,app_type='0')
            for to_do_list_instance in to_do_list_instances:       
                to_do_list_instance.finishDate  = timezone.now()
                to_do_list_instance.operator    = operator
                to_do_list_instance.ip          = ip
                # '-1' stand for this item has been deleted.
                to_do_list_instance.Status      = '-1'
                to_do_list_instance.save()
                
    def delete_Problem(self,app,ip,operator):
            to_do_list_instances= To_do_list.objects.filter(app_problem__exact=app,app_type='1')
            for to_do_list_instance in to_do_list_instances:       
                to_do_list_instance.finishDate  = timezone.now()
                to_do_list_instance.operator    = operator
                to_do_list_instance.ip          = ip
                # '-1' stand for this item has been deleted.
                to_do_list_instance.Status      = '-1'
                to_do_list_instance.save()        
    def get_all(self):
        to_do_list_all = To_do_list.objects.all()
        return to_do_list_all
    def get_list_type(self,type):
        to_do_list_type = To_do_list.objects.filter(type=type, Status='0')
        return to_do_list_type
    
    
