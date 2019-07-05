from . import views
from django.conf.urls import url
app_name='booktest'
#应用路由配置
urlpatterns=[
    #下面的应用路由对应视图函数，以后要添加视图函数的时候记得来配置应用路由
    #第一个是正则匹配url路径，第二参数是视图函数名
    url(r'^index/$',views.index,name='index'),
    url(r'^list/$',views.list,name='list'),
    #路由传参，参数写在视图函数的参数位置。而传过去的参数写在路由的最后边（用正则组的形式）
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
]

