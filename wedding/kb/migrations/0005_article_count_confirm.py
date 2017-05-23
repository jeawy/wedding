# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0004_kb_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='count_confirm',
            field=models.IntegerField(default=0, verbose_name='\u8ba4\u8bc1\u6570\u91cf'),
        ),
    ]
