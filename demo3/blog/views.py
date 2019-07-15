from django.shortcuts import render,reverse,redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from django.core.paginator import  Page,Paginator
from django.http import JsonResponse
# Create your views here.
class IndexView(View):
    def get(self,request):
        ads=Ads.objects.all()
        articles=Article.objects.all()
        #paginator有两个必填参数（对象列表，每页有几个对象）
        # paginator=Paginator(articles,2)
        #取当前页码(现在是没有给page传值，page=None)
        pagenum=request.GET.get('page')
        pagenum=1 if not pagenum else pagenum
        #由当前页码得到分页对象
        page=Paginator(articles,1).get_page(pagenum)
        print(page,type(page),'------------------------')
        return render(request,'blog/index.html',locals())
#详情页
class SingleView(View):
    #这是文章展示
    def get(self,request,id):
        article=Article.objects.get(pk=id)
        # print(article,'-----------')
        # print(article.comment_set.all()[0].content)
        return render(request,'blog/single.html',locals())
    #这个是提交表单之后的操作
    def post(self,request,id):
        article = Article.objects.get(pk=id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')
        # 然后存入数据库中。
        com = Comment()
        com.name = name
        com.url = url
        com.email = email
        com.content = comment
        com.article = article
        com.save()
        return redirect(reverse('blog:single', args=(id,)))
# 这个模型类是用于异步刷新接收ajax传过来的数据（和ajax进行交互的）
class AddComment(View):
     # 由于ajax的type使用的是post请求，所以我们只重写post方法。
     def post(self,request,id):
         # 通过get POST请求，得到ajax传过来的数据。
         #然后把接收到的数据存入数据库中
         article=Article.objects.get(pk=id)
         name=request.POST.get('name')
         email = request.POST.get('email')
         url = request.POST.get('url')
         comment = request.POST.get('comment')
         # 然后存入数据库中。
         com = Comment()
         com.name = name
         com.url = url
         com.email = email
         com.content = comment
         com.article = article
         com.save()
         create_time=com.create_time
         print(create_time)
         print(create_time.year,create_time.month,create_time.day,create_time.hour,create_time.minute,create_time.second)
         #note:我们可以把数据全传过去，也可以只传一个创建时间。
         return JsonResponse({'create_time':create_time})


