# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20170128_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo_comments',
            old_name='conmments',
            new_name='comments',
        ),
    ]
