from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from . import models
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import login ,logout,authenticate
from .类写表单 import *
#引入绘图模块
from PIL import Image,ImageDraw,ImageFont
import random,io
from django.core.cache import cache
from django.views.decorators.cache import cache_page
# Create your views here.
# note为了让每个页面都做到，没有登录就不让进入，直接返回登录页面。
#我们就用一个装饰器（闭包），来装饰每个视图函数，检查是否登录。
#装饰器的原理，给一个函数用@+外部闭包名，添加装饰器，，装饰器是一个闭包，闭包会自动把装饰的函数作为闭包外部函数的参数fun。
def checkLogin(fun):
    def check(request,*args):
        # 使用cookie获取信息
        # username=request.COOKIES.get('username')
        #使用session获取信息
        # username=request.session['username']
        # username=request.session.get('username')
        #系统user类检查登录
        username=request.user.is_authenticated
        if username:
            #request和args都是形参
            return fun(request,*args)
        else:
            return redirect(reverse('votetest:Login'))
    return check


@checkLogin
@cache_page(timeout=100)
def index(request):
    # print('000000000000000')
    # print(request.user,request.user.is_authenticated)#没有用户登录 requser.user为匿名用户
    # user=authenticate(request,username='admin1',password='123') #（获得授权用户）
    # #使用已有用户授权，授权成功则user=用户名，授权失败则user为None
    # # print(user)
    # print('111111111111111')
    # #note：不管我们是否获得授权用户，只要我们没有登录，调用request.user返回的都是匿名用户AnonymousUser，
    # #note：只要我们用授权用户登录login（request,user）在调用request.user就是用户名了。
    # print(request.user,request.user.is_authenticated)
    # # 授权成功user才有is_authenticated这个属性。
    # print(user,)
    # # print(user.is_authenticated) #有授权则，返回true。
    # if user:
    #     print(user,user.is_authenticated)
    #     #获得授权用户成功之后
    #     # 进行登录只需要调用人家封装号的登录函数，
    #     login(request,user)#内部原理，函数内部也是使用session进行存储一下。
    #     #重点来了，只要我们用授权用户登录login（request,user）在调用request.user就是用户名了。
    #     print(request.user,request.user.is_authenticated)
    # else:
    #     print('授权失败')

    #用COOKIES获得用户名，如果有用户登录就可以进入投票页，否则返回登录页。（也算是一种安全机制）
    # username = request.COOKIES['username'] #这种写法，取不到会报错
    #装饰器修饰前：
    # username=request.COOKIES.get('username')
    # if username :
    #     questions=VoteInfo.objects.all()
    #     return render(request,'votetest/index.html',locals())
    # else:
    #     return redirect(reverse('votetest:Login'))
    # 装饰器修饰后
    #获取cookies信息
    # username = request.COOKIES.get('username')
    #获取session信息
    # username = request.session.get('username') #我们使用系统自带的uesr登录方法，自己写的session先去掉
    questions = VoteInfo.objects.all()
    return render(request, 'votetest/index.html', locals())

    # locals() 所有局部变量以键值对的形式存在字典中
    # print(request,'--------')
    # print(dir(request))
    # questions=VoteInfo.objects.all()
    # return render(request,'votetest/index.html',locals())
@checkLogin
def choice(request,id):
    question = VoteInfo.objects.get(pk=id)
    if request.method == 'GET':
        # print(question.optioninfo_set.all(),'----------------------------------------')
        return render(request,'votetest/choice.html',locals())
    else:
        opid = request.POST.get('choice') #我们获得的是c.id
        #下面开始票数加1操作
        op=OptionInfo.objects.get(pk=opid)
        op.voteNum+=1
        op.save()
        #重定向到result页面,并且把question的id传过去
        return redirect(reverse('votetest:result',args=(id,)))
@checkLogin
def result(request,id):
    question=VoteInfo.objects.get(pk=id)
    # print(question.optioninfo_set.all(),'++++++++++++++++++++++++++++')
    return render(request,'votetest/result.html',locals())
def register(request):
    if request.method == 'GET':
        return render(request,'votetest/register.html')
    elif request.method == 'POST':
        #获取注册表单中的用户名，密码
        #用user类中自带的方法存入数据库中。Votetest.objects.creaete_user(username='',password='',email='')
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        email = request.POST.get('email')
        print(username,pwd,email,'-----------------')
        user=VotetestUser.objects.create_user(username=username,password=pwd,email=email)
        if user:
            return redirect(reverse('votetest:Login'))
        else:
            return HttpResponse('注册用户失败')
def Login(request):
    # note:cookie中的内容是在中python文件中写的。
    if request.method == 'GET':
        return render(request,'votetest/Login.html',locals())
    elif request.method == 'POST':
        #点击登录，接收到POST，开始进行下面操作。
        #首先检查用户名和密码是否存在
        #存在，登录成功需要存储cookie（需要调用响应的对象）
        # username=request.POST.get('username')
        # username=request.POST.get('username')
        # # print(username,'--------------++++++++-------------------')
        # response = redirect(reverse('votetest:index'))
        # response.set_cookie('username',username)
        # return response

        #使用session存储信息
        #存储设置session
        # request.session['username']=request.POST.get('username')
        # request.session['pwd']=request.POST.get('password')
        #设置cookie和session是为了，不让未登陆的人进入本网站的其他网页。
        #设计逻辑：-----首先验证数据库中的 用户名和密码。正确了才 设置cookie和session，不正确给提示。
        #用系统自带的user类登录
        # 首先获取登录表单
        username=request.POST.get('username')
        pwd = request.POST.get('password')
        print(username,pwd)
        # user = authenticate(request, username='admin1', password='123')
        user = authenticate(request,username=username,password=pwd)
        print(user,'=====================')
        if user:
            #下面是验证码信息，逻辑：如果验证码生成的字符串和我们从缓存中获得字符串（就是用户输入的在模板中用redis缓存的）相同。
            # 我们就验证成功，否则验证失败。
            # print(request.POST.get('verify'),'------------',cache.get('verify'))
            if request.POST.get('verify')==cache.get('verify'):
                login(request,user)#验证成功就登录
                return redirect(reverse('votetest:index'))

            else:
                return HttpResponse('验证失败！！')
        else:
            return redirect(reverse('votetest:Login'))
def LoginOut(request):
    # 清除cookie，并且同步到浏览器中。（浏览器中的cookie也删除）
    # return redirect(reverse('votetest:index'))
    #先用一个变量接收响应。然后信息处理（删除响应中的cookie，最后返回）
    # response=redirect(reverse('votetest:index'))
    # response.delete_cookie('username')
    # return response
    #清除session信息
    # request.session.flush() #使用user自带的 loginout方法
    #系统uesr类自带的logout方法（内部封装了清空session）
    logout(request)
    return redirect(reverse('votetest:Login'))
#验证码
def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('ariali.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')

    #将rand_str存入redis缓存中
    cache.set('verify',rand_str)
    print(rand_str,'ver中')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')