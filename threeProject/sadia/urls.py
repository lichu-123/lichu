from django.conf.urls import url
from . import views
app_name='sadia'
urlpatterns = [
    url('^index/$', views.index, name='index'),
    url('^Login/$',views.Login,name='Login'),
    url('^register/$', views.register, name='register'),
    url('^LoginOut/$',views.LoginOut,name='LoginOut'),
    url('^shop/$', views.shop, name='shop'),
    url('^searchBrand/(\d+)/$', views.searchBrand, name='searchBrand'),
    url('^searchCategorie/(\d+)/$', views.searchCategorie, name='searchCategorie'),
    url('^searchTag/(\d+)/$', views.searchTag, name='searchTag'),
    url('^active/(.*?)/$', views.active, name='active'),
]