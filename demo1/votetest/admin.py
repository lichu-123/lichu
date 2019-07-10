from django.contrib import admin
from .models import *

class OptionInfolines(admin.StackedInline):
    model = OptionInfo #模型是谁
    extra = 1 #extra额外的（有几个默认字段）

class VoteInfoAdmin(admin.ModelAdmin):

    list_display = ('info',)#重写(系统类ModelAdmin中的)list_display
    list_filter = ('info',)#增加过滤器 (后面可以增加)
    # list_per_page = 1 #分页，一页显示一本
    inlines = [OptionInfolines,]

class OptionInfoAdmin(admin.ModelAdmin):
    #重写(系统类ModelAdmin中的)list_display
    list_display = ('name','voteNum',)
    search_fields = ('name','voteNum',)#fields（字段搜索（），根据字段的汉字模糊搜素

# Register your models here.
#把我们用model生成的数据库表注册到admin中
admin.site.register(VoteInfo,VoteInfoAdmin)
admin.site.register(OptionInfo,OptionInfoAdmin)
admin.site.register(Ads)