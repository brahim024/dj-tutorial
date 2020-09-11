from django.views.generic import ListView
from django.shortcuts import render

from myapp.models import Book, Publisher
class PublisherList(ListView):
	model=Publisher
	context_object_name='publisher'
	queryset=Publisher.objects.all()



