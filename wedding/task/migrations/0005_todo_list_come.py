# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_remove_todo_list_come'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_list',
            name='come',
            field=models.CharField(default=b'0', max_length=10, choices=[(b'0', '\u7537\u65b9'), (b'1', '\u5973\u65b9')]),
        ),
    ]
