# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('photo', models.CharField(max_length=120, verbose_name='\u81ea\u5b9a\u4e49\u5934\u50cf')),
                ('age', models.DateField(verbose_name='\u751f\u65e5')),
                ('starcount', models.IntegerField(verbose_name='\u661f\u661f\u6570')),
                ('loginname', models.CharField(max_length=30, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=30, verbose_name='\u5bc6\u7801')),
                ('superdaddy', models.CharField(max_length=30, verbose_name='\u7279\u6743')),
                ('telphone', models.CharField(max_length=30, verbose_name='\u624b\u673a\u53f7')),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(verbose_name='\u663e\u793a\u6216\u9690\u85cf')),
                ('token', models.CharField(max_length=30, verbose_name='\u5fae\u4fe1\u5fae\u535a\u652f\u4ed8\u5b9d')),
                ('addtime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30, verbose_name='\u59d3\u540d')),
                ('sort', models.IntegerField(verbose_name='\u6392\u5e8f\u503c')),
                ('stime', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('etime', models.DateField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
                ('addtime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_delete', models.BooleanField(verbose_name='\u662f\u5426\u5220\u9664')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tname', models.CharField(max_length=30, verbose_name='\u7c7b\u522b\u540d')),
                ('info', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('difficulty', models.IntegerField(verbose_name='\u96be\u5ea6\u503c')),
                ('star', models.IntegerField(verbose_name='\u661f\u661f\u503c')),
                ('icont', models.CharField(max_length=30, verbose_name='\u56fe\u6807')),
                ('sort', models.IntegerField(verbose_name='\u6392\u5e8f\u503c')),
                ('is_delete', models.BooleanField(verbose_name='\u662f\u5426\u5220\u9664')),
                ('addtime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('t_pid', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='v1.Type', verbose_name='\u4e0a\u7ea7\u7c7b\u578b')),
                ('uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='list',
            field=models.ManyToManyField(to='v1.Type'),
        ),
        migrations.AddField(
            model_name='plan',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Person'),
        ),
    ]
