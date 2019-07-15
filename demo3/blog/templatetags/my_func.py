"""

自定义模板表达式
扩展Django原有功能

"""
from django.template import library
register=library.Library()
from blog.models import Article

# (建立一个简单的模板标签，可以在模板中直接使用)  note：注意，不要搞混模板和模型。（模板时html模型是搞数据库的）
#使用方法：只需要在模板中（html中）加载一下就能直接用了。（{% load my_func %}）
@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by('-create_time')[:num]

#自定义过滤器
@register.filter
def myjoin(value,spl):
    return spl.join(value)


