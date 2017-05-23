# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_dataplace_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coveredrate',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='dataplace',
            options={'ordering': ['-id']},
        ),
    ]
