# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20170105_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataplace',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
