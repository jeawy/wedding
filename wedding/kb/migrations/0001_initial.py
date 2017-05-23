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
            name='Active_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('deadline', models.DateField(verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xa5\xe6\x9c\x9f')),
                ('number', models.SmallIntegerField(default=100, verbose_name='\u6d3b\u52a8\u4e0a\u9650\u4eba\u6570')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Active_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='\u53d1\u8868\u65e5\u671f')),
                ('title', models.CharField(max_length=1024, verbose_name='\u6807\u9898')),
                ('desc', models.TextField(default=b'', verbose_name='\u6458\u8981')),
                ('count_read', models.IntegerField(default=0, verbose_name='\u9605\u8bfb')),
                ('count_good', models.IntegerField(default=0, verbose_name='\u8d5e')),
                ('count_reply', models.IntegerField(default=0, verbose_name='\u56de\u590d')),
                ('top_pic', models.ImageField(upload_to=b'article', null=True, verbose_name='\u9876\u56fe')),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u72b6\u6001')),
                ('is_essence', models.SmallIntegerField(default=0, verbose_name='\u7cbe\u534e\u8d34')),
                ('dt_set_essence', models.DateTimeField(null=True, verbose_name='\u8bbe\u7f6e\u7cbe\u534e\u7684\u65e5\u671f')),
                ('type', models.SmallIntegerField(default=0, verbose_name='\u5e16\u5b50\u7c7b\u578b')),
                ('url', models.TextField(null=True, verbose_name='\u5546\u57ce\u94fe\u63a5')),
                ('money', models.SmallIntegerField(null=True, verbose_name='\u4ed3\u5e93\u5e01')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('cannot_publish_kb', '\u9ed1\u540d\u5355:\u4e0d\u80fd\u53d1\u5e16\uff0c\u4e0d\u80fd\u56de\u5e16'), ('cannot_modify_kb', '\u4fee\u6539\u5e16\u5b50\u6743\u9650:\u6ca1\u6709\u6743\u9650\u4fee\u6539\u5e16\u5b50'), ('can_modify_all_kb_top_pic', '\u53ef\u4ee5\u8bbe\u7f6e\u6240\u6709\u5e16\u5b50\u7684\u9876\u56fe'), ('can_modify_all_kb', '\u7ba1\u7406\u5458\u53ef\u4ee5\u4fee\u6539\u6240\u6709\u4eba\u7684\u8d34\u5b50'), ('can_del_all_kb', '\u7ba1\u7406\u5458\u53ef\u4ee5\u5220\u9664\u6240\u6709\u4eba\u7684\u8d34\u5b50'), ('manage_all_kb', '\u7ba1\u7406\u8d34\u5b50\uff1a\u5220\u9664\uff0c\u8bbe\u4e3a\u7cbe\u534e\uff0c\u8bbe\u7f6e\u8f6e\u64ad\u56fe.')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('kb', models.ForeignKey(to='kb.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreeGift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.SmallIntegerField(default=100, verbose_name='\u793c\u54c1\u6570\u91cf')),
                ('min_level', models.SmallIntegerField(default=0, verbose_name='\u4f1a\u5458\u7b49\u7ea7')),
                ('kb', models.ForeignKey(to='kb.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreeGift_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('kb', models.ForeignKey(to='kb.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kb_Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money', models.SmallIntegerField(verbose_name='\u6253\u8d4f\u91d1\u989d')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kb', models.ForeignKey(to='kb.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kb_Collect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kb', models.ForeignKey(to='kb.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kb_Recommend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_block', models.CharField(default=b'0', max_length=10, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe8\x87\xb3\xe6\x9d\xbf\xe5\x9d\x97')),
                ('type_homepage_slice', models.CharField(default=b'0', max_length=10, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe8\x87\xb3\xe9\xa6\x96\xe9\xa1\xb5\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe')),
                ('type_homepage_kb', models.CharField(default=b'0', max_length=10, verbose_name=b'\xe6\x8e\xa8\xe8\x8d\x90\xe8\x87\xb3\xe9\xa6\x96\xe9\xa1\xb5\xe5\xb8\x96\xe5\xad\x90\xe5\x88\x97\xe8\xa1\xa8')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kb', models.ForeignKey(to='kb.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.ImageField(upload_to=b'article', verbose_name=b'')),
                ('status', models.SmallIntegerField(default=0, verbose_name='\u56fe\u7247\u72b6\u6001')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'', verbose_name=b'')),
                ('num', models.SmallIntegerField(default=1, verbose_name=b'\xe5\xba\x8f\xe5\x8f\xb7')),
                ('article', models.ForeignKey(to='kb.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pic',
            name='slices',
            field=models.ForeignKey(to='kb.Slice'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pic',
            name='uploader',
            field=models.ForeignKey(related_name='pic_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='active_user',
            name='kb',
            field=models.ForeignKey(to='kb.Article'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='active_user',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='active_info',
            name='kb',
            field=models.ForeignKey(to='kb.Article'),
            preserve_default=True,
        ),
    ]
