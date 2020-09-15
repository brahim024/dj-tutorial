#from django.views.generic.base import TemplateView
from django.shortcuts import render ,get_object_or_404
#from django.views import View
#from django.http import HttpResponseForbidden,HttpResponsePermanentRedire
# from django .urls import reverse
from myapp.models import Post
def post_list(request):
	posts=Post.objects.all()
	return render(request,'post_list.html',{'posts':posts})
def post_details(request,year,month,day ,post):
	post=get_object_or_404(Post,slug=post,
								status='published',
								publish__year=year,
								publish__month=month,
								publish__day=day)
	return render(request,'post_details.html',{'post':post})




								