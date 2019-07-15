from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse
class ArticleFeed(Feed):
    title='LC的博客'
    description='介绍一些开发知识'
    link='/'
    #重写items方法，返回前三篇文章
    def items(self):
        return Article.objects.order_by('-create_time')[:3]
    #重写item_title方法，返回标题
    def item_title(self, item):
        return item.title
    def item_link(self,item):
        return reverse('blog:single',args=(item.id,))
    def item_description(self, item):
        return item.author.username+':'+item.title

    #然后我们需要提供一个路由供人家使用。



