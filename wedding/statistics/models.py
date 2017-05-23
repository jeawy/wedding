from django.db import models

# Create your models here.
class Stat(models.Model):
    url   = models.CharField(max_length=64)
    count = models.IntegerField(default=1)

    
    def __unicode__(self):
        return self.url
