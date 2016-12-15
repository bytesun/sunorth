from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Club(models.Model):
    CLUB_TYPES_CHOICES=(
        (1,_("Hiking")),
        (2,_("Camping")),
        (3,_("Sailing")),
        (4,_("Rowing")),
        (5,_("Skiing")),
        (6,_("Biking")),
        (7,_("Fishing")),
        (0,_("Other"))
        )
    name = models.CharField(max_length=100)
    ctype = models.IntegerField(choices=CLUB_TYPES_CHOICES,default=0)
    description = RichTextUploadingField()
    website = models.URLField(null=True,blank=True)
    language = models.CharField(max_length=10,default='en-us') 
    createdate = models.DateField(default=timezone.now)