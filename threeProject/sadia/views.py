from django.shortcuts import render,reverse,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.core.paginator import Page,Paginator
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from threeProject.settings import *
#在规定时间内有效
from itsdangerous import TimedJSONWebSignatureSerializer
# Create your views here.


#分页函数
def getpage(request,object_list,per_num):
    pagenum= request.GET.get('page')
    pagenum=1 if not pagenum else pagenum
    page=Paginator(object_list,per_num).get_page(pagenum)#paginator第一个参数是有几个对象，第二个参数是对象里边有几个列表
    return page

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
        ##发送邮件测试
        # send_mail()发送邮件有且只有4个必填参数（主题，信息，发送者，接受者列表）
        # reclist = ['1278822679@qq.com','b1278822679@163.com']
        # try:
        #     send_mail('Python测试邮件', '这是一封python测试邮件',EMAIL_HOST_USER,reclist)
        # except BaseException as e:
        #     print(e)
        ##发送的内容支撑html标签的发送方式
        #腾讯强大的安全功能，直接把我发的邮件丢进了垃圾箱子，并且链接点不开。
        # reclist = ['b1278822679@163.com']
        # mail=EmailMultiAlternatives('Python测试邮件33','<a href="https://www.baidu.com">百度一下</a>',EMAIL_HOST_USER,reclist)
        # mail.content_subtype='html'
        # mail.send()
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
            user.is_active=False
            user.save()
            #发送邮件
            # 创建一个序列化工具
            serializer = TimedJSONWebSignatureSerializer(SECRET_KEY)
            serializerstr = serializer.dumps({"userid": user.id}).decode("utf-8")
            reclist = [email]
            mail=EmailMultiAlternatives('账号激活','<a href="http://127.0.0.1:8000/active/%s/">点击激活账号</a>'%(serializerstr),EMAIL_HOST_USER,reclist)
            mail.content_subtype='html'
            mail.send()
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
    page = getpage(request, goods_list, 9)
    return render(request,'sadia/shop.html',locals())
def searchBrand(request,id):
    goods_list=Brand.objects.get(pk=id).goods_set.all()
    # print(goods_list)
    page = getpage(request, goods_list, 9)
    return render(request, 'sadia/shop.html', locals())
def searchCategorie(request,id):
    goods_list=Categorie.objects.get(pk=id).goods_set.all()
    # print(goods_list)
    page = getpage(request, goods_list, 9)
    return render(request, 'sadia/shop.html', locals())
def searchTag(request,id):
    goods_list=Tag.objects.get(pk=id).goods_set.all()
    # print(goods_list)
    page = getpage(request, goods_list, 9)
    return render(request, 'sadia/shop.html', locals())

#账号激活
def active(request, id):
    print('----------------')
    serializer = TimedJSONWebSignatureSerializer(SECRET_KEY)
    serializerobj = serializer.loads(id)
    id = serializerobj["userid"]

    user = get_object_or_404(MyUser, pk=id)
    user.is_active = True
    user.save()

    return redirect(reverse('sadia:Login',))