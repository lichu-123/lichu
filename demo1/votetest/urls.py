from .views import *
from django.conf.urls  import *
from . import views
app_name='votetest'
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^choice/(\d+)/$',views.choice,name='choice'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^Login/$',views.Login,name='Login'),
    url(r'^LoginOut$',views.LoginOut,name='LoginOut'),
]

