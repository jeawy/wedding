# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_auto_20170208_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo_list',
            options={'ordering': ['-date', 'status'], 'permissions': (('manage_todolist', 'Can manage TODO list'),)},
        ),
    ]
