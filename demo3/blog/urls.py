from django.conf.urls import url,include
from . import views
from .feeds import ArticleFeed
app_name='blog'
urlpatterns=[
    #首页
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name='single'),
    url(r'^rss/$',ArticleFeed()),
    #这个路由用于接收异步刷新，接收ajax传的数据。(需要传文章id)
    url(r"^addcomment/(\d+)/$",views.AddComment.as_view(),name='addcomment')

    # url(r"^addcomment/(\d+)/$",views.AddComment.as_view(),name='addcomment'),
    #一会要写一个添加文章的页面  url(r'^detail/(\d+)/$'
    # url(r'^addarticle/$',views.AddArticleView.as_view(),name='addarticle'),
    # url(r'^ueditor$','DjangoUeditor.urls',name='ueditor')
]