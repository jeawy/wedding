# -*- coding:utf-8 -*-
import smtplib
from email import encoders
from email import Utils
from email.message import Message
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart  
from email.MIMEText import MIMEText
from django.conf import settings
import pdb
 
class EmailEx(object):
    def send_text_email(self,Subject,content,receiver):
        if settings.EMAIL_SWITCH:
            sender              = 'postmaster@map2family.com'
            themsg              = MIMEMultipart()
            themsg['Subject']   = Subject
            themsg['To']        = receiver
            themsg['From']      = u'吃典网'
            themsg['Date']      = Utils.formatdate(localtime = 1)
            themsg['Message-ID'] = Utils.make_msgid()
            msgAlternative      = MIMEMultipart('alternative')
            themsg.attach(msgAlternative)
            content = content + '<br/>www.lechier.com'
            msgText = MIMEText(content,'html', 'utf-8')
            msgAlternative.attach(msgText)
            themsgtest = themsg.as_string() 
            # send the message
            server = smtplib.SMTP()  
            server.connect(settings.SMTP_SERVER) 
            server.login(settings.SMTP_SERVER_USER, settings.SMTP_SERVER_PWD)
            server.sendmail(sender, receiver, themsgtest)
            server.quit()#SMTP.quit()
            
