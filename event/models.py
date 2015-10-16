from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Event(models.Model):
    subject =  models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    description = RichTextUploadingField()
    do_time = models.DateTimeField(editable=True)
    owner = models.ForeignKey(User, null=True)
    
    def __unicode__(self):
        return self.subject
        
    def get_absolute_url(self):
        return reverse('event_info',  kwargs={'id': self.pk})    