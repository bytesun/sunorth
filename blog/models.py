from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=10,default='zh-cn')
    def __str__(self):
        return self.name
        
# Create your models here.
class Blog(models.Model):
    subject =  models.CharField(max_length=500)
    tags = models.ManyToManyField(Tag)
    content = RichTextUploadingField()
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User, null=True)
    language = models.CharField(max_length=10,default='zh-cn')
    
    def __unicode__(self):
        return self.subject
        
    def get_absolute_url(self):
        return reverse('blog_info',  kwargs={'id': self.pk})    
        
    def __str__(self):
        return self.subject    
        
class Comment(models.Model):
    comment = models.TextField()
    create_time = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)   
    
    def __str__(self):
        return self.comment       


class News(models.Model):
    title = models.CharField(max_length=300)
    content =  RichTextUploadingField()
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User, null=True)
    language = models.CharField(max_length=10,default='zh-cn')