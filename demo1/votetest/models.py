from django.db import models


# MVT中的M 数据库模型
# ORM对象
# Create your models here.

# 创建一个投票信息(模型类)
class VoteInfo(models.Model):
    # 投票信息
    info = models.CharField(max_length=50)
    # 默认当成当前创建的时间。(出版时间)
    crerate_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.info


# 创建一个选项表（模型类） option: 选项，选择权。
class OptionInfo(models.Model):
    # 姓名、性别、内容、书的id（级联删除）
    name = models.CharField(max_length=20)
    # gender = models.BooleanField(default=True)
    # content = models.CharField(max_length=100)
    # 外键，我们在添加数据库的时候写 h1.book=b1(赋值是实例，这样数据表中会自动和另一个表相结合，字段为我们需要找的外键)
    # 级联删除
    voteNum = models.IntegerField(default=0)
    info = models.ForeignKey(VoteInfo, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name

# note：创建完模型类之后，需要把模型类生成迁移文件同步到表里边。
class Ads(models.Model):
    desc=models.CharField(max_length=20)
    img=models.ImageField(upload_to='ads')
    def __str__(self):
        return self.desc