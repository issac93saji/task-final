from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models



class Events(models.Model):
    events_name=models.CharField(max_length=100)
    events_def=models.CharField(max_length=200)
    events_date_added=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.events_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    title=models.CharField(max_length=100, default='', null=True,blank=True )
    profile_image=models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
       return self.user.username



class Comments(models.Model):
    data=models.CharField(max_length=100)
    events_date_added=models.DateTimeField(auto_now_add=True)
    # uid=models.OneToOneField(UserProfile,blank=False)
    uid=models.ManyToManyField(UserProfile)
    events=models.ManyToManyField(Events,blank=False)
    def __unicode__(self):
       return self.data

class Contact(models.Model):
    mail=models.EmailField(blank=False,null=False)
    data=models.CharField(max_length=200,null=False,blank=False)
    def __unicode__(self):
       return self.data