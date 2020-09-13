from django.views.generic import DetailView ,ListView
from django.shortcuts import render

from myapp.models import Book, Publisher ,Author

class PublisherList(ListView):
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