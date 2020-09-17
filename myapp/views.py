#from django.views.generic.base import TemplateView
from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
 									PageNotAnInteger
from django.views.generic import ListView
from myapp.models import Post
from django.core.mail import send_mail
from .forms import EmailPostForm

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
	return render(request,'post_list.html',{'posts':posts,'page':page})
#her we have details function
def post_details(request,year,month,day ,post):
	post=get_object_or_404(Post,slug=post,
								status='published',
								publish__year=year,
								publish__month=month,
								publish__day=day)
	return render(request,'post_details.html',{'post':post})
#return pagination aith class based views
class PostListView(ListView):
	queryset=Post.objects.all()
	context_object_name='posts'
	paginate_by= 2
	template_name='post_list.html'
def post_share(request,post_id):
	post=get_object_or_404(Post,id=post_id,status='published')
	sent=False
	#retrieve post by id
	if request.method=='POST':
		form=EmailPostForm(request.POST)
		cd =form.cleaned_data
		#send email
		post_url=request.build_absolute_url(post.get_absolute_url())
		subjects=f"{cd ['name']} recommends your red"\
				 f"{post.title}"
		message = f"Read {post.title} at {post_url}\n\n" \
 				  f"{cd['name']}\'s comments: {cd['comments']}"
 		send_mail(subject, message, 'boughanm6@gmail.com' ,
 						  [cd['to']])
 		sent = True
	else:
		form =EmailPostForm
	return render(request,'share.html',{'post':post ,
										'form':form,
										'sent':sent})

								