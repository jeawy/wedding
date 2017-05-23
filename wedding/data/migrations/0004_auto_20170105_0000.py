# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20170104_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='coveredrate',
            name='city_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coveredrate',
            name='county_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coveredrate',
            name='province_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
