from django.contrib import admin
from .models import *

class HeroInfolines(admin.StackedInline):
    model = HeroInfo #模型是谁
    extra = 1 #extra额外的（有几个默认字段）

class BookInfoAdmin(admin.ModelAdmin):

    list_display = ('title','pub_date')#重写(系统类ModelAdmin中的)list_display
    list_filter = ('title','pub_date')#增加过滤器 (后面可以增加)
    # list_per_page = 1 #分页，一页显示一本
    inlines = [HeroInfolines,]

class HeroInfoAdmin(admin.ModelAdmin):
    #重写(系统类ModelAdmin中的)list_display
    list_display = ('name','content','gender')
    search_fields = ('name','content')#fields（字段搜索（），根据字段的汉字模糊搜素

# Register your models here.
#把我们用model生成的数据库表注册到admin中
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(Ads)