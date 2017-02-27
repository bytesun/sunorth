from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class ATag(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=10,default='zh-cn')
    def __str__(self):
        return self.name
        

# Create your models here.
class Activity(models.Model):
    subject =  models.CharField(max_length=500)
    tags = models.ManyToManyField(ATag,null=True)
    description = RichTextUploadingField(null=True)
    do_time = models.DateField(null=True) # xxxx
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)    
    owner = models.ForeignKey(User, null=True) #xxxx
    organizer = models.CharField(max_length=50,default='xxx@sunorth.org')
    participants = models.CharField(null=True, max_length=1000)    
    language = models.CharField(max_length=10,default='en-us') #xxxx
    
    def __unicode__(self):
        return self.subject
    
        
    def get_absolute_url(self):
        return reverse('activity_info',  kwargs={'id': self.pk})    
        
class Comment(models.Model):
    comment = models.TextField()
    create_time = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User,related_name='activity_owner')
    activity = models.ForeignKey(Activity)  
    
    def __str__(self):
        return self.comment      