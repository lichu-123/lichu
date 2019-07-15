from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
class SimpleMiddleware(MiddlewareMixin):
    #请求和响应函数
    def process_request(self,request):
        print('处理了请求')
        print(request.headers)
        print(request.headers.get('User-Agent'))
    def process_response(self,request,response):
        print('处理了响应')
        return response
#定义完类之后在settings中引入我们自己定义的中间件