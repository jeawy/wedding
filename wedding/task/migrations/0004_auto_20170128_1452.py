# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20170128_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_comments',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
