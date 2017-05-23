# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_coveredrate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataProvince',
            new_name='DataPlace',
        ),
    ]
