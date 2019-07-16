from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import *
# Create your views here.
#写一个装饰器来检查登录
def checklogin(fun):
    def check(request,*args):
        username=request.user.is_authenticated
        if username:
            #如果有用户登录，则返回本视图函数,否则重定向到登录页面
            return fun(request,*args)
        else:
            return redirect(reverse('sadia:Login'))
    return check

def Login(request):
    if request.method == 'GET':
        return render(request,'sadia/login.html',locals())
    elif request.method == 'POST':
        # 首先接收登录表单传过来的值，用户名密码。
        username = request.POST.get('login_username')
        pwd = request.POST.get('login_password')
        print(username,pwd,'-------------')
        user=authenticate(request,username=username,password=pwd)
        print(user)
        if user:
            login(request,user)
            return redirect(reverse('sadia:index'))
        else:
            return redirect(reverse('sadia:Login'))
def register(request):
    if request.method == 'GET':
        return render(request, 'sadia/register.html', locals())
    elif request.method == 'POST':
        #首先接收注册表单传过来的值，用户名密码。
        username = request.POST.get('username')
        pwd = request.POST.get('login_password')
        email = request.POST.get('login_email')
        #note:注册之前要先判定注册的用户存在不存在。
        test_list=MyUser.objects.all()
        # print(test_list)
        # print(type(test_list),'---------------')
        for i in test_list:
            # print(i.username)
            if i.username == username:
                print('您注册的用户名已存在')
                return redirect(reverse('sadia:register', ))
        else:
            user=MyUser.objects.create_user(username=username, email=email, password=pwd)
            print(user)
            return redirect(reverse('sadia:Login',))
@checklogin
def index(request):
    return render(request,'sadia/index.html',locals())
def LoginOut(request):
    logout(request)
    return redirect(reverse('sadia:Login', ))
def shop(request):
    goods_list=Goods.objects.all()
    # for a in goods_list:
    #     print(a.name,'------------------------')
    # print(goods_list)
    return render(request,'sadia/shop.html',locals())


