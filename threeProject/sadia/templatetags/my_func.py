"""
自定义模板表达式
扩展Django原有功能
"""
# 模板标签
#
from django.template import library
register = library.Library()
from sadia.models import Categorie,Brand,Goods,Tag

@register.simple_tag
def getBrand(num=5):
    # print('111111')
    # print(Brand.objects.all(),'-----------')
    return  Brand.objects.all()
@register.simple_tag
def getCategorie(num=5):
    return  Categorie.objects.all()
@register.simple_tag
def getTag(num=5):
    return  Tag.objects.all()
# @register.simple_tag
# def PriceLTH(num=5):
#     return  Goods.objects.order_by("price")
# def PriceHTL(num=5):
#     return  Goods.objects.order_by("-price")