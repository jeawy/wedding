# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import auth


from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
)


class MapFamilyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password, name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    model for User, using the column 'email' for primary key and login to our web site.
    """
    name            = models.CharField( u'姓名',max_length=50,default=u'未填写')
    email           = models.EmailField(
        verbose_name= u'电子邮箱',
        max_length=255,
        unique=True,
    )
	 
    date            = models.DateTimeField(u'注册日期', auto_now_add = False) 
    is_active       = models.BooleanField( u'是否有效',default=True)
    is_admin        = models.BooleanField( u'是否为管理员',default=False)
    
	
    #identify is user saved the portraint they uploaded
    #True: they saved
    #False: by default, they didn't save
    is_head_portrait     = models.BooleanField(u'是否保存了上传后的头像',default=False)
    #the filename of portrait is something like: userid_*****.***, the prefix is userid, and then with 5 random chars.
    #ex:1_sdfs2.jpg 
    head_portrait   	 = models.ImageField(u'选择头像',  upload_to='portrait',default='/static/img/portraint.jpg')	
    #fake_head_portrait   = models.ImageField(u'未保存的头像',  upload_to='portrait',default='/media/portrait/no_img/no_portrait1.jpg')
    
	#definitions for social users
    email_verified       = models.BooleanField(u'是否保存了邮箱',default=False)
    #0 for not social user, 1 for user, 2 for both user
    social_user_status   = models.IntegerField(u'第三方用户状态',default=0)
    social_site_name     = models.IntegerField( u'第三方名称',default=0)#1 for qq          
    social_user_id       = models.CharField( u'第三方用户ID',max_length=255,default=u'未填写') 
    
	#this is the thumbnail of user protrait
    #the filename of thumbnail portrait is something like: userid_thumbnl_*****.***, the prefix is userid, and then with 5 random chars.
    #these five random chars are the same with the portrait.
    #ex:1_thumbnl_sdfs2.jpg 
    thumbnail_portait    = models.ImageField(u'头像缩略图',  upload_to='portrait',default='/static/img/portraint.jpg')
    
    #If there is message for this user, this column will be marked as TRUE; else will be marked as FALSE
    msg_mark             = models.BooleanField(u'有新消息', default=False)

    
    
    objects              = MapFamilyUserManager()

    USERNAME_FIELD       = 'email'
    REQUIRED_FIELDS      = ['name']

    def get_name(self):
        # The user is identified by their email address
        return self.name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        #return True
        """
        Returns True if the user has the specified permission. This method
        queries all available auth backends, but returns immediately if any
        backend returns True. Thus, a user who has permission from a single
        auth backend is assumed to have permission in general. If an object is
        provided, permissions for this specific object are checked.
        """

        # Active superusers have all permissions.
        if self.is_active and self.is_superuser:
            return True

        # Otherwise we need to check the backends.
        return _user_has_perm(self, perm, obj)
    
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    def get_short_name(self):
        # The user is identified by their email address
        return self.name
    def get_full_name(self):
        # The user is identified by their email address
        return self.name
    
    class Meta:
            permissions = (
                ("admin_management", "manage group, permission and user"),
                
            )
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_active
    def get_full_name(self):
        # The user is identified by their email address
        return self.name
    
def _user_has_perm(user, perm, obj):
    """
    A backend can raise `PermissionDenied` to short-circuit permission checking.
    """
    for backend in auth.get_backends():
        if not hasattr(backend, 'has_perm'):
            continue
        try:
            if backend.has_perm(user, perm, obj):
                return True
        except PermissionDenied:
            return False
    return False


class VerifyCode(models.Model):
    """
    the random code used to verify the email validation  
    """
    email = models.EmailField(
        max_length=255,
    )
    #the random code
    code = models.CharField( u'code',max_length=50,default=u'')
    #type = 0, the code used for register
    #type = 1, the code used to find password
    type = models.CharField( u'type',max_length=5,default='0')
