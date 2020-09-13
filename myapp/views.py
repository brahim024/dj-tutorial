from django.views.generic.base import TemplateView
#from django.shortcuts import render
#from django.views import View
#from django.http import HttpResponseForbidden,HttpResponsePermanentRedire
# from django .urls import reverse
from myapp.models import Author

'''class PublisherList(ListView):
	model= Publisher
	context_object_name='my_favorite_publisher'
class PublisherDetail(DetailView):
	context_object_name='publisher'
	queryset=Publisher.objects.all()
	def get_context_data(self, **kwargs):
		# call the base implimentation first to get context
		context=super().get_context_data(**kwargs)
	 	#add in queryset of all the book
		context['book_list']=Book.objects.all()
		return context
		
class AuthorList(ListView):
	model=Author
	context_object_name='author'


class RecordInterest(SingleObjectMixin, View):
	models=Author
	def post (self,request ,*args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object=self.get_object() #here we search for authers
		return HttpResponsePermanentRedirect(reverse('author-detail',kwargs={'pk':self.object.pk}))
''' 
class AuthorView(TemplateView):
	template_name='myapp/author2.html'
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['authors']=Author.objects.get(id=1)
		context['data']="Context Data for Author"
		return context