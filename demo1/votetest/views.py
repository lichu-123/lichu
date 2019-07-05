from django.shortcuts import render,redirect,reverse
from .models import *


# Create your views here.
def index(request):
    # locals() 所有局部变量以键值对的形式存在字典中
    questions=VoteInfo.objects.all()
    return render(request,'votetest/index.html',locals())
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
def result(request,id):
    question=VoteInfo.objects.get(pk=id)
    # print(question.optioninfo_set.all(),'++++++++++++++++++++++++++++')
    return render(request,'votetest/result.html',locals())


