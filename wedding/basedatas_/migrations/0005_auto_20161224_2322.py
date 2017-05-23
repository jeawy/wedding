# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatas', '0004_auto_20151229_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_words',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reltn_dayword_comm',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='reltn_dayword_comm',
            name='day_word',
        ),
        migrations.DeleteModel(
            name='Day_words',
        ),
        migrations.DeleteModel(
            name='Reltn_dayword_comm',
        ),
    ]
