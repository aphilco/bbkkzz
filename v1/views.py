# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader, RequestContext
from django.shortcuts import render,redirect
from django.db import models
from v1.forms import typeadd,userli,plangroup
from v1.models import Person,Type,Plan,Logdone
import datetime,re,os



# Create your views here.

def home(request):
    userid = 1;#获得用户id
    nowtime = datetime.datetime.now()#获取当前日期
    #获得当天计划清单（当前用户下，开始日期小于当日，结束日期大于当日的计划内容）：
    p_home_list = Plan.objects.filter(uname=userid).exclude(stime__gt=nowtime).exclude(etime__lt=nowtime).distinct()
    #获得当天已完成的计划（完成日志表）
    loglist = Logdone.objects.filter(uname=userid,logtime=nowtime)
    #如果结果为空，则定义一个空值
    jli = []
    #不为空
    if loglist.exists():
        #则将donelist值读取后，转换为字符串，
        numli = str(loglist[0])
        #通过正则，形成新的格式列表n
        f = re.compile(r'\,')
        n = f.split(numli)
        #新的列表元素是字符，所以需要转换为数字，方便前台判断，显示是否已经勾选了
        for ll in n:
            jli.append(int(ll))
    #当天计划完成进度：
    aa = len(p_home_list)
    bb = len(numli)
    if bb == 0 :
        cc = 0
    else:
        cc = round(bb/float(aa),2)*100

    #创建前台显示字典
    context = {
        'plist':p_home_list,
        'numli':jli,
        'jindu':cc,
    }

    return render(request,'home.html',context)


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



def type_add(request,user_id):
    form = typeadd(request.POST)
    if form.is_valid():
        tname = form.cleaned_data['tname']
        t_pid = form.cleaned_data['t_pid']
        addtime = form.cleaned_data['addtime']
        uname = form.cleaned_data['uname']
        isdelete = form.cleaned_data['is_delete']
        info = form.cleaned_data['info']
        icont = form.cleaned_data['icont']
        difficulty = form.cleaned_data['difficulty']
        star = form.cleaned_data['star']
        sort = form.cleaned_data['sort']

        Type.objects.create(tname=tname,t_pid=t_pid,addtime=addtime,uname=uname,is_delete=isdelete,info=info,icont=icont,difficulty=difficulty,star=star,sort=sort,)
        return redirect('/bkz/type/1')

    context = {
        'form':form,
    }

    return render(request, 'type_test.html', context,
                  context_instance=RequestContext(request))

def type_edit(request,type_id):
    typecontent = Type.objects.get(pk=type_id)
    #tpid =
    form = typeadd(request.POST or None,initial={'t_pid':typecontent.t_pid})
    if request.method=='POST':
        typecontent.tname = request.POST['tname']
        #typecontent.t_pid = typeadd(request.POST or None).cleaned_data['t_pid']
        #addtime = form.cleaned_data['addtime']
        #uname = form.cleaned_data['uname']
        isdelete = request.POST['is_delete']
        if isdelete==''  :
            typecontent.isdelete = 0
        else:
            typecontent.isdelete = 1
        typecontent.info = request.POST['info']
        typecontent.icont = request.POST['icont']
        typecontent.difficulty = request.POST['difficulty']
        typecontent.star = request.POST['star']
        typecontent.sort = request.POST['sort']
        typecontent.save()
        #Type.objects.get_or_create(pk=type_id,tname=tname,t_pid=t_pid,addtime=addtime,is_delete=isdelete,info=info,icont=icont,difficulty=difficulty,star=star,)
        return redirect('/bkz/type/1')

    numli = [0,1,2,3,4,5,]

    context = {
        'form':form,
        'nodes': typecontent,
        'numli':numli
    }

    return render(request, 'type_edit.html', context,)

def planlist(request,user_id):
    planli = Plan.objects.filter(uname= user_id)
    #typegrou = Type.objects.get
    return render(request,'plan.html', {'nodes':planli},
                          context_instance=RequestContext(request))


def planadd(request,user_id):
    form = plangroup(request.POST)
    if form.is_valid():
        pname = request.POST['pname']
        addtime = form.cleaned_data['addtime']
        listid = request.POST.getlist('list')
        uname = form.cleaned_data['uname']
        isdelete = request.POST['is_delete']
        sort = request.POST['sort']
        stime = request.POST['stime']
        etime = request.POST['etime']
        qqqq = Plan.objects.create(pname=pname,addtime=addtime,uname=uname,is_delete=isdelete,sort=sort,stime=stime,etime=etime)
        #listgroup = Type.objects.filter(id=listid)
        #print listgroup
        #listid = (1,2,5,6,7,9)
        for i in listid:
            qqqq.list.add(i)



        return redirect('/bkz/plan/1')

    context = {
        'form':form,
    }
    return render(request,'plan_add.html', context,
                          context_instance=RequestContext(request))

def planedit(request,plan_id):
    planli = Plan.objects.get(pk=plan_id)
    listgroup = plangroup(request.POST,initial={'pname':planli.id})

    if listgroup.is_valid():
        # planli.pname = request.POST['pname']
        # planli.addtime = listgroup.cleaned_data['addtime']
        # #listid = request.POST.getlist('list')
        # planli.isdelete = request.POST['is_delete']
        # planli.sort = request.POST['sort']
        # planli.stime = request.POST['stime']
        # planli.etime = request.POST['etime']

        # planli.save()

        #for i in listid:
        #    planli.list.add(i)
        return render(request,'temp.html',)

    context = {
        'form': planli,
        'tlist':listgroup,
    }
    return render(request, 'plan_edit.html', context,
                  context_instance=RequestContext(request))

#edit don't done
def planedit1(request,plan_id):
    planli = Plan.objects.get(pk=plan_id)
    listgroup = plangroup(request.POST,initial={'pname':planli.id})


    planli.pname = request.POST['pname']
    #planli.addtime = request.POST['addtime']
    listid = request.POST.getlist('list')
    planli.isdelete = request.POST['is_delete']
    planli.sort = request.POST['sort']
    planli.stime = request.POST['stime']
    planli.etime = request.POST['etime']

    #planli.save()

    plantype = Plan.objects.filter(pk=plan_id).save(planli)
    plantype.list.add(i)

    context = {
        'form': planli,
        'tlist': listgroup,
    }
    return render(request, 'plan.html', context,
                  context_instance=RequestContext(request))

def planinfo(request,plan_id):
    plancontent = Plan.objects.get(pk=plan_id)
    listgroup = plangroup(request.POST)
    context = {
        'form': plancontent,
        'tlist': listgroup,
    }
    return render(request,'plan_info.html', context,
                  context_instance=RequestContext(request))