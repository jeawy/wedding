# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '__first__'),
        ('basedatas', '0003_day_words'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reltn_dayword_comm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='reltn_dayword_comm',
            name='comment',
            field=models.ForeignKey(to='comment.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reltn_dayword_comm',
            name='day_word',
            field=models.ForeignKey(to='basedatas.Day_words'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day_words',
            name='comment_count',
            field=models.IntegerField(default=0, verbose_name=b'count for comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='day_words',
            name='good_count',
            field=models.IntegerField(default=0, verbose_name=b'count for praise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_words',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
