# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from v1.models import Person,Type,Plan,Logdone
from mptt.admin import MPTTModelAdmin
# Register your models here.

class PersonAadmin(admin.ModelAdmin):
    list_display = ('uname','starcount','telphone','addtime')

class TypeAdmin(admin.ModelAdmin):
    list_display = ('tname','star','t_pid')



class PlanAdmin(admin.ModelAdmin):
    list_display = ('pname','uname')


class LogdoneAadmin(admin.ModelAdmin):
    list_display = ('logtime','pname','uname')

admin.site.register(Person,PersonAadmin)
admin.site.register(Type,MPTTModelAdmin)
admin.site.register(Plan,PlanAdmin)
admin.site.register(Logdone,LogdoneAadmin)