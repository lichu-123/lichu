from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
from django.views.generic import View,TemplateView,ListView
# from django.shortcuts import render
# Create your views here.
#note：视图函数必须有参数
def index(request):
    return render(request,'booktest/index.html',{'username':'lc'})
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
