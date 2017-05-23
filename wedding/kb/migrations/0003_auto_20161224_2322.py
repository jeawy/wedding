# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb', '0002_auto_20160327_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_user',
            name='kb',
        ),
        migrations.RemoveField(
            model_name='book_user',
            name='user',
        ),
        migrations.AlterField(
            model_name='article',
            name='top_pic',
            field=models.ImageField(upload_to=b'article', null=True, verbose_name='\u7f29\u7565\u56fe'),
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.TextField(null=True, verbose_name='\u5916\u90e8\u94fe\u63a5'),
        ),
        migrations.DeleteModel(
            name='Book_user',
        ),
    ]
