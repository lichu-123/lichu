from django.shortcuts import render,redirect,reverse,get_object_or_404
from .models import *
from . import models
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.contrib.auth import login ,logout,authenticate
from .类写表单 import *

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
        username=request.session.get('username')
        if username:
            #request和args都是形参
            return fun(request,*args)
        else:
            return redirect(reverse('votetest:Login'))
    return check


@checkLogin
def index(request):
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
    username = request.COOKIES.get('username')
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
        request.session['username']=request.POST.get('username')
        return redirect(reverse('votetest:index'))

def LoginOut(request):
    # 清除cookie，并且同步到浏览器中。（浏览器中的cookie也删除）
    # return redirect(reverse('votetest:index'))
    #先用一个变量接收响应。然后信息处理（删除响应中的cookie，最后返回）
    response=redirect(reverse('votetest:index'))
    response.delete_cookie('username')
    return response
