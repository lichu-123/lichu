from django.db import models
from django.contrib.auth.models import User
# from DjangoUeditor.models import UEditorField
# Create your models here.

#种类（jewelery(珠宝)、表（watches）、dresses（连衣裙）,handbag(手提包)，accessories（配饰））
class Categorie(models.Model):
    title=models.CharField(max_length=20,default='nnn')
    # goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    def __src__(self):
        return self.title
#标签
class Tag(models.Model):
    title=models.CharField(max_length=10,default='nnn')
    # goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    def __src__(self):
        return self.title

#品牌（Nike、Sadia、Lorem、Ipsum、Dolet）
class Brand(models.Model):
    title=models.CharField(max_length=10,default='nnn')
    # goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    def __src__(self):
        return self.title
#分类 women,s tops等
class Classify(models.Model):
    title=models.CharField(max_length=20,default='nnn')
    # goods = models.ForeignKey(Goods, on_delete=models.PROTECT)
    def __src__(self):
        return self.title

#商品
class Goods(models.Model):
    name=models.CharField(max_length=20)#名字
    price=models.IntegerField(default=0)#价格
    addTime=models.DateTimeField(auto_now_add=True)#上架时间（新品）
    desc=models.TextField()#介绍
    size=models.CharField(max_length=10)#尺寸
    #图片字段
    img1=models.ImageField(upload_to='goods')#图片要上传到的位置
    img2 = models.ImageField(upload_to='goods')
    img3 = models.ImageField(upload_to='goods')
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)#类型（jewelery(珠宝)、表（watches）、dresses（连衣裙）,
    tag=models.ManyToManyField(Tag)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    saveNum=models.IntegerField(default=0)
    classify=models.ForeignKey(Classify,on_delete=models.CASCADE)
    #浏览量
    view=models.IntegerField(default=0)
    #购买量
    payNum=models.IntegerField(default=0)
    #添加购物车次数
    addCartNum=models.IntegerField(default=0)

    # handbag(手提包)，accessories（配饰））
    # goods=models.ForeignKey(Goods,on_delete=models.CASCADE)
    # def __src__(self):
    #     return self.name

#用户类
class MyUser(User):
    telephone=models.CharField(max_length=11)
