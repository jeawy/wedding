from django.db            import models
from area.models          import Area
from administration.models import User

class Words(models.Model):
    keywords = models.CharField(max_length=2048, null= True)
    area     = models.ForeignKey(Area, null= True)
    ip       = models.CharField(max_length = 48, null = True)
    user     = models.ForeignKey(User, null= True)
    date     = models.DateTimeField(auto_now_add = True)
    class Meta:
        ordering = ['-date']