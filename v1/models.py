# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# -*- coding: UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Person(models.Model):
    uname = models.CharField(u"姓名",max_length=30)
    photo = models.CharField(u'自定义头像',max_length=120,blank=True)
    age = models.DateField(u'生日')
    starcount = models.IntegerField(u'星星数',blank=True,default=0)
    loginname = models.CharField(u"用户名",max_length=30)
    password = models.CharField(u"密码",max_length=30)
    superdaddy = models.CharField(u"特权",max_length=30)
    telphone = models.CharField(u"手机号",max_length=30,blank=True)
    email = models.EmailField()
    status = models.BooleanField(u'显示或隐藏')
    token = models.CharField(u"微信微博支付宝",max_length=30,blank=True)
    addtime = models.DateField(u'创建时间')


    def __unicode__ (self):
        return self.uname




class Type(MPTTModel):
    tname = models.CharField(u"类别名",max_length=30)
    t_pid = TreeForeignKey("self", blank=True, null=True, related_name="children",verbose_name='上级类型')
    info = models.TextField(u'描述', blank=True)
    difficulty = models.IntegerField(u'难度值', blank=True,default=0)
    star = models.IntegerField(u'星星值', blank=True,default=0)
    icont = models.CharField(u"图标",max_length=30, blank=True)
    sort = models.IntegerField(u'排序值', blank=True, default=30)
    is_delete = models.BooleanField(u'是否删除')
    addtime = models.DateField(u'创建时间')
    uname = models.ForeignKey(Person)

    class MPTTMeta:
        parent_attr = 't_pid'
        order_insertion_by = 'sort'

    def __unicode__(self):
        return self.tname

class Plan(models.Model):
    pname = models.CharField(u"姓名",max_length=30)
    uname = models.ForeignKey(Person)
    list = models.ManyToManyField(Type)
    sort = models.IntegerField(u'排序值', blank=True, null=True,default=30)
    stime = models.DateField(u'开始时间')
    etime = models.DateField(u'结束时间')
    addtime = models.DateField(u'创建时间')
    is_delete = models.BooleanField(u'是否删除')

    def __unicode__ (self):
        return self.pname

