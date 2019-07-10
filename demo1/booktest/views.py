from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from django.views.generic import View,TemplateView,ListView
# from django.shortcuts import render
# Create your views here.
#note：视图函数必须有参数
def index(request):
    return render(request,'booktest/index.html',{'username':'lc','ads':Ads.objects.all()})
    # return render(request,'blog/index.html',content)
def list(request):
    books=BookInfo.objects.all()
    return render(request,'booktest/list.html',{'books':books})
def detail(request,id):
    book=BookInfo.objects.get(pk=id)
    # print(book)
    return render(request, 'booktest/detail.html', {'book':book})

def deletebook(request,id):
    BookInfo.objects.get(pk=id).delete()
    #重定向，回到list页面
    return redirect( reverse('booktest:list'))
def addhero(request,id):
    book = BookInfo.objects.get(pk=id)
    #这个是进入页面所要做的
    if request.method == 'GET':
        return render(request,'booktest/addhero.html',{"book":book})
    #这个是点击添加按钮所要做的
    elif request.method == 'POST':
        name=request.POST.get('username')
        content=request.POST.get('content')
        # gender=request.POST.get('gender')
        # gender1 = request.POST.get('gender1')
        hero = HeroInfo()
        hero.name=name
        hero.content=content
        hero.book=book
        # hero.gender=gender
        # hero.type=gender1
        hero.save()
        # print('我出来了啊')
        return redirect(reverse('booktest:detail',args=(id,)))

def deletehero(request,id):
    # 因为我们要删除的是book中的某个英雄所以,从我们表的结构来看，删除英雄并不需要知道是那本书。
    hero=HeroInfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    # hero.save() #删除不用.save() 推测，修改和添加需要.save()要调用一个保存函数。 而.delete()的传到数据库已经写在其中了。
    #重定向的原理，并不是刷新了页面。
    return redirect(reverse('booktest:detail',args=(bookid,)))
def addbook(request):
    if request.method == 'GET':
        return render(request,'booktest/addbook.html')
    else:
        title=request.POST.get('title')
        book=BookInfo()
        book.title=title
        book.save()
        return redirect(reverse('booktest:list',))

def model_index(request):
    return render(request,'booktest/model_index.html')



