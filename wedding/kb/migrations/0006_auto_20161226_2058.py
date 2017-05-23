# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_auto_20161221_2335'),
        ('kb', '0005_article_count_confirm'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.ForeignKey(to='area.Area')),
            ],
        ),
        migrations.CreateModel(
            name='FoodPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=2048)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='higher_price',
            field=models.DecimalField(null=True, verbose_name='\u53c2\u8003\u4ef7\u683c\u8303\u56f4\uff1a', max_digits=9, decimal_places=2),
        ),
        migrations.AddField(
            model_name='article',
            name='lower_price',
            field=models.DecimalField(null=True, verbose_name='\u53c2\u8003\u4ef7\u683c\u8303\u56f4\uff1a', max_digits=9, decimal_places=2),
        ),
        migrations.AddField(
            model_name='foodplace',
            name='kb',
            field=models.ForeignKey(to='kb.Article'),
        ),
        migrations.AddField(
            model_name='foodlocation',
            name='kb',
            field=models.ForeignKey(to='kb.Article'),
        ),
    ]
