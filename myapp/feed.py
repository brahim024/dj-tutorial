from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from djnago.urls import reverse_lazy
from.models import Post

#craete feed class

class LatestPostfeed(Feed):
	title='My blog'
	link=reverse_lazy('blog:post_list')
	description='New posts of my blog '

	def items(self):
		return Post.objects.all()[:5]

	def item_description(self,item):
		return truncatewords(items.body,30)
