import xadmin
from .models import *
# xadmin.site.register('**')
#注册模型类
xadmin.site.register(Category)
xadmin.site.register(Tag)
#注册模板时，添加模型的后台管理类，在管理类中声明需要使用富文本的字段。
class ArticleAdmin:
    #模型字段想要使用ueditor样式必须注册模型管理类
    style_fields = {'body':'ueditor'}

xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ads)