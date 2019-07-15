from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.
#轮播图
class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20)
    index=models.IntegerField(default=0)
    def __str__(self):
        return self.desc
#category ：种类分类。
class Category(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
#标签
class Tag(models.Model):
    title=models.CharField(max_length=10)
    def __str__(self):
        return self.title
#文章
class Article(models.Model):
    #文章标题
    title=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#文章分类
    create_time=models.DateTimeField(auto_now_add=True)#创建时间
    update_time=models.DateTimeField(auto_now=True)#更新时间
    #User类是系统自带的
    author=models.ForeignKey(User,on_delete=models.CASCADE)#作者
    views=models.IntegerField(default=0) #阅读数
    # body=models.TextField()
    #换成富文本形式
    body=UEditorField()#文章内容
    #多对多
    tags=models.ManyToManyField(Tag)#文章对应的标签
    def __str__(self):
        return self.title
class Comment(models.Model):
    create_time=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=20)
    url=models.URLField(blank=True,null=True,default='http://www.baidu.com')
    email=models.EmailField(blank=True,null=True)
    content=models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE)