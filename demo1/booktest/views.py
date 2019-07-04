from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    # return HttpResponse('<strong>hello world</strong>') #返回一个基本标签
    today='今天是个好天气！<a href="/blog/first/"> 跳转到首页</a>'
    content={'today':today}
    return render(request,'blog/index.html',content) #note：返回的时候不需要把html的详细路径写下来，只需要把templates目录下的相对路径链接写下来就行。
    # return render(request, 'blog/index.html', {'today':'今天是晴天ma '}) #实验的出这一句和前一句的结果是一样的
def register(request):
    return HttpResponse('注册')
def first(request):
    # 1.获取模板
    temp1 = loader.get_template('blog/first.html')
    # 2.使用模板渲染字典
    result = temp1.render({'book':'这是一本好书'})
    # 3.将渲染的结果返回
    return HttpResponse(result)
    # return HttpResponse('首页 <a href="/blog/list/"> 跳转到列表页</a> <a href="/blog/index/"> 跳转到index页</a> ')
def list(request):
    # s="""
    #     <br>
    #     <a href='/blog/detail/1'>跳转到详情页1</a>
    #     <br>
    #     <a href='/blog/detail/2'>跳转到详情页2</a>
    #     <br>
    #     <a href='/blog/detail/3'>跳转到详情页3</a>
    # """
    # return  HttpResponse('列表页 <a href="/blog/detail/"> 跳转到详情页</a>')
    # return HttpResponse('列表页 %s'%s)
    # 1.获取模板
    temp1 = loader.get_template('blog/list.html')
    # 2.使用模板渲染字典
    result = temp1.render({})
    # 3.将渲染的结果返回
    return HttpResponse(result)
def detail(request,id):
    # return  HttpResponse('详情页%s <a href="/blog/first/"> 跳转到首页</a>'%id)
    # 1.获取模板
    temp1 = loader.get_template('blog/detail.html')
    # 2.使用模板渲染字典
    result = temp1.render({})
    # 3.将渲染的结果返回
    return HttpResponse(result)


