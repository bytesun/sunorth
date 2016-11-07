from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class ATag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
# Create your models here.
class Activity(models.Model):
    subject =  models.CharField(max_length=500)
    tags = models.ManyToManyField(ATag)
    description = RichTextUploadingField()
    do_time = models.DateField()
    owner = models.ForeignKey(User, null=True)
    language = models.CharField(max_length=10,default='zh-cn')
    
    def __unicode__(self):
        return self.subject
    def __str__(self):
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