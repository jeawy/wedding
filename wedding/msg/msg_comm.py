from .models import Msg


class MsgComm(object):
    """
    the common operations class
    """
    '''
    @staticmethod
    def add(owner_in, url_in,  msgtext_in):
        """
        add new msg to database
        parameters:
        #owner, whom the msg will be sent to
        #url, the destination msg will jump to  
        #piclink, whom the msg will be sent to       
        """
        try:
            #add msg to DB
            msg = Msg.objects.create(owner =owner_in, url = url_in, msgtext = msgtext_in )
            msg.save()
        except:
            print '[msg][ERROR] Failed to add msg to database.'
    '''
    @staticmethod
    def add(owner_in, url_in, piclink_in, msgtext_in, type_in ):
        """
        add new msg to database
        parameters:
        #owner, whom the msg will be sent to
        #url, the destination msg will jump to  
        #piclink, whom the msg will be sent to       
        """
        try:
            #add msg to DB
            msg = Msg.objects.create(owner =owner_in, url = url_in, piclink = piclink_in, msgtext = msgtext_in, type = type_in )
            msg.save()
        except:
            print '[msg][ERROR] Failed to add msg to database.'
        
    @staticmethod
    def delete(id):
        """
        not really delete the msg, just make it invisible to the owner
        """
        try:
            msg = Msg.objects.get(pk = id)
            msg.visibility = False # the owner has handled the msg
            msg.save()
        except Msg.DoesNotExist:
            #can't get this id
            print '[msg][ERROR]can\'t get this id: ', id