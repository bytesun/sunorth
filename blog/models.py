from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    subject =  models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    content = models.TextField()
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User, null=True)
    
    def __unicode__(self):
        return self.subject
        
    def get_absolute_url(self):
        return reverse('blog_info',  kwargs={'id': self.pk})    
        
class Comment(models.Model):
    comment = models.TextField()
    create_time = models.DateTimeField(default=timezone.now,editable=True)
    owner = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)    


