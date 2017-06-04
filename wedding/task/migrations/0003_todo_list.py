# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_delete_todo_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xa5\xe6\x9c\x9f')),
                ('name', models.CharField(max_length=1000, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('phone', models.CharField(default=b'', max_length=1000, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('address', models.TextField(default=b'', verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80\xe5\x8f\x8a\xe7\x95\x99\xe8\xa8\x80')),
                ('whichside', models.CharField(default=b'0', max_length=10, choices=[(b'0', '\u7537\u65b9'), (b'1', '\u5973\u65b9')])),
                ('come', models.CharField(default=b'0', max_length=10, choices=[(b'0', '\u7537\u65b9'), (b'1', '\u5973\u65b9')])),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
