from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Gallery(models.Model):
    photo = models.ImageField(upload_to='gallery/%Y/%m/%d')
    story = models.CharField(max_length=200)
    
    rate = models.IntegerField(default=0)
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    photographer = models.ForeignKey(User)
