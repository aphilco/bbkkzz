# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader, RequestContext
from django.shortcuts import render,redirect
from django.db import models
from v1.forms import typeadd,userli
from v1.models import Person,Type
import datetime



# Create your views here.

def home(request):
    return render(request,'home.html')


def userinfo(request,user_id):
    if str(user_id) == '0':
        return render(request, "userinfo.html")
    user = Person.objects.get(pk=user_id)
    return render(request,"userinfo.html",{'user':user})

def user_edit(request,user_id):#修改个人信息
    user = Person.objects.get(pk=user_id)
    uname = request.POST['uname']
    if uname : #若昵称修改，则赋值
        user.uname = uname
    user.age = request.POST.get('age', '2012-03-18')
    user.telphone = request.POST.get('telphone', '18909691724')
    user.status = request.POST.get('status', '1' )
    user.save()
    return render(request, "home.html")


def typelist(request,user_id):
    typeli = Type.objects.filter(uname= user_id)
    return render(request,'type.html', {'nodes':typeli},
                          context_instance=RequestContext(request))

def tp_add(request,user_id):
    form = typeadd(request.POST)
    typeli = Type.objects.filter(uname=user_id)
    return render(request, 'type_test.html', {'nodes': typeli},
                  context_instance=RequestContext(request))

def type_add(request,user_id):
    form = typeadd(request.POST)
    if form.is_valid():
        tname = form.cleaned_data['tname']
        t_pid = form.cleaned_data['t_pid']
        addtime = form.cleaned_data['addtime']
        uname = form.cleaned_data['uname']
        isdelete = form.cleaned_data['is_delete']
        Type.objects.create(tname=tname,t_pid=t_pid,addtime=addtime,uname=uname,is_delete=isdelete)
        return redirect('/bkz/type/1')

    typeli = Type.objects.filter(uname=user_id)
    context = {
        'form':form,
        'nodes': typeli,
    }

    return render(request, 'type_test.html', context,
                  context_instance=RequestContext(request))



    #Type.objects.get_or_create(tname=tname,is_delete=0,addtime=datetime.datetime.now(),uname=uname.id)
    #Type.objects.create(tname=tname,t_pid=tid,is_delete=0)
