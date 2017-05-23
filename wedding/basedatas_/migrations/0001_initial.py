# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name=b'comment')),
                ('type', models.CharField(max_length=1, verbose_name=b'type')),
                ('Comment_date', models.DateTimeField(verbose_name=b'comment date')),
                ('App_id', models.IntegerField(verbose_name=b'app id')),
                ('Commenter_type', models.CharField(default=b'0', max_length=1, verbose_name=b'Commenter type')),
                ('commenter', models.ForeignKey(verbose_name=b'commenter', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
