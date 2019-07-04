from django.conf.urls import include, url
# 它访问到的是我们views（当前视图中的index函数），所以要导入当前路径下的views
from . import views

# 应用配置路由
urlpatterns = [
    #当放访问该网址会，执行视图函数。
    url(r'^index/$', views.index),
    url(r'^first/$', views.first),
    url(r'^list/$', views.list),
    #路由传递视图参数
    url(r'^detail/(\d+)/$', views.detail),
    #能不能进入某个页面，访问地址是否有路由能够匹配成功
]

