# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoveredRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('province_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('city_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('county_rate', models.DecimalField(max_digits=5, decimal_places=2)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
