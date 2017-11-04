# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logdone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logtime', models.DateField(verbose_name='\u8bb0\u5f55\u65f6\u95f4')),
                ('donelist', models.CharField(max_length=150, verbose_name='\u5b8c\u6210\u60c5\u51b5')),
                ('startcount', models.IntegerField(blank=True, default=30, verbose_name='\u661f\u661f\u6570')),
                ('addtime', models.DateField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.CharField(blank=True, max_length=120, verbose_name='\u81ea\u5b9a\u4e49\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='person',
            name='starcount',
            field=models.IntegerField(blank=True, default=0, verbose_name='\u661f\u661f\u6570'),
        ),
        migrations.AlterField(
            model_name='person',
            name='telphone',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='person',
            name='token',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u5fae\u4fe1\u5fae\u535a\u652f\u4ed8\u5b9d'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='etime',
            field=models.DateField(blank=True, null=True, verbose_name='\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='pname',
            field=models.CharField(max_length=30, verbose_name='\u8ba1\u5212\u540d'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sort',
            field=models.IntegerField(blank=True, default=30, null=True, verbose_name='\u6392\u5e8f\u503c'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='stime',
            field=models.DateField(blank=True, null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='type',
            name='difficulty',
            field=models.IntegerField(blank=True, default=0, verbose_name='\u96be\u5ea6\u503c'),
        ),
        migrations.AlterField(
            model_name='type',
            name='icont',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u56fe\u6807'),
        ),
        migrations.AlterField(
            model_name='type',
            name='info',
            field=models.TextField(blank=True, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='type',
            name='sort',
            field=models.IntegerField(blank=True, default=30, verbose_name='\u6392\u5e8f\u503c'),
        ),
        migrations.AlterField(
            model_name='type',
            name='star',
            field=models.IntegerField(blank=True, default=0, verbose_name='\u661f\u661f\u503c'),
        ),
        migrations.AddField(
            model_name='logdone',
            name='pname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Plan'),
        ),
        migrations.AddField(
            model_name='logdone',
            name='uname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.Person'),
        ),
    ]