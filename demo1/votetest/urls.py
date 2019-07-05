from .views import *
from django.conf.urls  import *
app_name='votetest'
urlpatterns = [
    url(r'^index/$',view=index,name='index'),
    url(r'^choice/(\d+)/$',view=choice,name='choice'),
    url(r'^result/(\d+)/$',view=result,name='result'),

]