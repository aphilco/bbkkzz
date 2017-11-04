from django.conf.urls import include, url
from v1 import views

urlpatterns = [
    url(r'^index/$',views.home,name='home'),
    url(r'^userinfo/(?P<user_id>[0-9]+)$',views.userinfo,name='userinfo'),
    url(r'^edit/(?P<user_id>[0-9]+)$',views.user_edit,name='user_edit'),
    url(r'^type/(?P<user_id>[0-9]+)$',views.typelist,name='typelist'),
    url(r'^typeadd/(?P<user_id>[0-9]+)$',views.type_add,name='typeadd'),
    url(r'^typeedit/(?P<type_id>[0-9]+)$',views.type_edit,name='typeedit'),
    url(r'^plan/(?P<user_id>[0-9]+)$',views.planlist,name='planlist'),
    url(r'^planadd/(?P<user_id>[0-9]+)$',views.planadd,name='planadd'),
    url(r'^planedit/(?P<plan_id>[0-9]+)$',views.planedit,name='planedit'),
    url(r'^planinfo/(?P<plan_id>[0-9]+)$',views.planinfo,name='planinfo'),
]