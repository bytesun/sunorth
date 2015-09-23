from django.db import models

class Case(models.Model):
    
    subject = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    description = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True,auto_now=False)
    
    def __unicode__(self):
        return self.subject
