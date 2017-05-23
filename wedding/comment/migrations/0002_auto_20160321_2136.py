# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='kb',
            field=models.ForeignKey(verbose_name=b'\xe5\xb8\x96\xe5\xad\x90', to='kb.Article', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
