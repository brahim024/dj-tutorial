#from django.views.generic.base import TemplateView
from django.shortcuts import render 
from django.core.paginator import Paginator, EmptyPage,\
 									PageNotAnInteger
#from django.views.generic import ListView
#from django.views import View
#from django.http import HttpResponseForbidden,HttpResponsePermanentRedire
# from django .urls import reverse
from myapp.models import Post
'''class PostListView(ListView):
	queryset=Post.objects.all()
	context_object_name='posts'
	paginate_by= 2
	template_name='myapp/author1.html'''
def post_list(request):
	object_list=Post.objects.all()
	paginator=Paginator(object_list,2) #her we want 2 objects(post)
	page=request.GET.get('page')
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		#if oage in not integer delivred the first page
		posts=paginator.page(1)
	except EmptyPage:
		#if page has out of range
		posts=paginator.page(paginator.num_pages)
	return render(request,'post_list.html',{'posts':posts})




def post_details(request,year,month,day ,post):
	post=get_object_or_404(Post,slug=post,
								status='published',
								publish__year=year,
								publish__month=month,
								publish__day=day)
	return render(request,'post_details.html',{'post':post})





								