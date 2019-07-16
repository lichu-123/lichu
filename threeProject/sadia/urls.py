from django.conf.urls import url
from . import views
app_name='sadia'
urlpatterns = [
    url('^index/$', views.index, name='index'),
    url('^Login/$',views.Login,name='Login'),
    url('^register/$', views.register, name='register'),
    url('^LoginOut/$',views.LoginOut,name='LoginOut'),
    url('^shop/$', views.shop, name='shop'),

]