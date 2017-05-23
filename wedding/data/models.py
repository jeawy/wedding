#-*- coding: utf8 -*-
from django.db import models

from area.models  import Area

class DataPlace(models.Model):
    """
    记录已经覆盖的省级、市级、县级城市
    无重复数据
    """
    area = models.ForeignKey(Area)
    num  = models.IntegerField(default = 0)
    class Meta:
        ordering = ['-id']


class CoveredRate(models.Model):
    province_rate = models.DecimalField(max_digits=5, decimal_places=2)
    province_count = models.PositiveIntegerField(default = 0)
    city_rate     = models.DecimalField(max_digits=5, decimal_places=2)
    city_count = models.PositiveIntegerField(default = 0)
    county_rate   = models.DecimalField(max_digits=5, decimal_places=2)
    county_count = models.PositiveIntegerField(default = 0)
    date          = models.DateField(auto_now_add = True)
    class Meta:
        ordering = ['-date']