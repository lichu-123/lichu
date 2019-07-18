from django.contrib import admin
from .models import *

# class HeroInfolines(admin.StackedInline):
#     model = HeroInfo #模型是谁
#     extra = 1 #extra额外的（有几个默认字段）

# class BookInfoAdmin(admin.ModelAdmin):
#     list_display = ('title','pub_date')#重写(系统类ModelAdmin中的)list_display
#     list_filter = ('title','pub_date')#增加过滤器 (后面可以增加)
#     # list_per_page = 1 #分页，一页显示一本
#     inlines = [HeroInfolines,]

# class CategorieLines(admin.StackedInline):
#     model = Categorie
#     extra = 1
# class TagLines(admin.StackedInline):
#     model = Tag
#     extra = 1
# class BrandLines(admin.StackedInline):
#     model = Brand
#     extra = 1
# class SaveNumLines(admin.StackedInline):
#     model = SaveNum
#     extra = 1
# class ClassifyLines(admin.StackedInline):
#     model = Classify
#     extra = 1
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name','addTime',)
    list_filter =  ('name','addTime',)
    list_per_page = 5 #分页
    # inlines = [CategorieLines,BrandLines,TagLines,SaveNumLines,ClassifyLines]
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10 #分页
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10 #分页
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10 #分页
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10 #分页
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Goods,GoodsAdmin)#商品
admin.site.register(Categorie,CategorieAdmin)#商品类型
admin.site.register(Tag,TagAdmin)#标签
admin.site.register(Brand,BrandAdmin)#品牌
admin.site.register(Classify,ClassifyAdmin)#分类
