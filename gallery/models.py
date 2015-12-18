from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class Gallery(models.Model):
    photo = ImageField(upload_to='gallery/%Y/%m/%d')
    story = models.CharField(max_length=200)
    
    rate = models.IntegerField(default=0)
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    photographer = models.ForeignKey(User)

    def __unicode__(self):
            return self.story
    def __str__(self):
        return self.story