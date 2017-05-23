# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20161221_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataProvince',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(to='area.Area')),
            ],
        ),
    ]
