from django.db import models
#MVT中的M 数据库模型
#ORM对象
# Create your models here.

#创建一个book信息(模型类)
class BookInfo(models.Model):
    #书的标题
    title = models.CharField(max_length=20)
    #默认当成当前创建的时间。(出版时间)
    pub_date = models.DateTimeField(auto_now=True)

#创建一个英雄hero信息（模型类）
class HeroInfo(models.Model):
    #姓名、性别、内容、书的id（级联删除）
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,)

#note：创建完模型类之后，需要把模型类生成迁移文件同步到表里边。
