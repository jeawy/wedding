# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20170128_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='status',
            field=models.CharField(default=b'0', max_length=10, choices=[(b'0', '\u672a\u5f00\u59cb'), (b'1', '\u6b63\u5728\u8fdb\u884c'), (b'2', '\u5df2\u5b8c\u6210')]),
        ),
        migrations.AlterField(
            model_name='todo_list',
            name='title',
            field=models.CharField(default=b'\xe4\xbb\xbb\xe5\x8a\xa1\xe5\x90\x8d\xe7\xa7\xb0', max_length=1000, verbose_name=b'\xe5\xbe\x85\xe5\x8a\x9e\xe4\xbb\xbb\xe5\x8a\xa1'),
        ),
    ]
