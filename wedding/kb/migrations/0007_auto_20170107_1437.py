# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0006_auto_20161226_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='i_ate',
            field=models.IntegerField(default=0, verbose_name='\u5403\u8fc7'),
        ),
        migrations.AddField(
            model_name='article',
            name='i_want',
            field=models.IntegerField(default=0, verbose_name='\u60f3\u5403'),
        ),
    ]
