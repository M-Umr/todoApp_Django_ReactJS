#from django.db import models
#from django.conf import settings
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from rest_framework.authtoken.models import Token
#from django.contrib.auth.models import (
 #   BaseUserManager, AbstractBaseUser
#)

#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
 #   if created:
  #      Token.objects.create(user=instance)


#class MyAccountManager(BaseUserManager):
 #   def create_user(self, email, password=None):
  #      if not email:
   #         raise ValueError('Users must have an email address')

    #    user = self.model(
     #       Email_Address=self.normalize_email(email),
      #      name=self.normalize_email(email),
            #Date_of_Birth=birthday,
            #zipcode=zipcode,
       # )

        #user.set_password(password)
        #user.save(using=self._db)
        #return user

    ##def create_superuser(self, Email_Address, password):
      #  user = self.create_user(
       #     Email_Address=self.normalize_email(Email_Address),
        #    password=password,
        #)
        #user.is_admin = True
        #user.is_active=True
        #user.is_staff = True
        #user.is_superuser = True
        #user.save(using=self._db)

#class Users(AbstractBaseUser):
 #   Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    #Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    #name = models.CharField(max_length=30, blank=True, null=True)
    #username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    #zipcode = models.CharField(max_length=30, blank=True, null=True)
    #is_admin = models.BooleanField(default=False)
    #is_active = models.BooleanField(default=True)
    #is_teacher = models.BooleanField(default=False)
  #  is_staff = models.BooleanField(default=False)
   # is_super_teacher = models.BooleanField(default=False)
    #is_superuser = models.BooleanField(default=False)

    #USERNAME_FIELD = 'Email_Address'

    #objects = MyAccountManager()

    #class Meta:
     #   db_table = "tbl_users"

    #def __str__(self):
     #   return str(self.email)


    #def has_perm(self, perm, obj=None): return self.is_superuser

    #def has_module_perms(self, app_label): return self.is_superuser
    
    
    
    
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title