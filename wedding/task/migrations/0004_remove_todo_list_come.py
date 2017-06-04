# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_todo_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='come',
        ),
    ]
