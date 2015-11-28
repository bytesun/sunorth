from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Topic(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=50)
    createtime = models.DateTimeField(default=timezone.now,editable=True)
    author = models.ForeignKey(User, null=True)

