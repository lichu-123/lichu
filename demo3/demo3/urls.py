"""demo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import xadmin
from django.conf.urls import url,include
#这个是用来管理上传的文件
from django.views.static import serve
from .settings import MEDIA_ROOT
urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
    url('blog/',include('blog.urls',namespace='blog')),
    path('ueditor/',include('DjangoUeditor.urls')),
    # 意思一旦我们搜索search执行的路由会到haystack下的urls里面。所有的搜索结果回到SearchView()里面
    #这个都对应上了我们在seach下新建的模板，这也是我们要按固定模式建模板的原因。（要和人家配好的模板相对应）
    url(r'^search/',include('haystack.urls')),

]





