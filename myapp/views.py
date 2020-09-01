from django.http import Http404
from django.shortcuts import render
from .models import Artist
# Create your views here.
def artists(request):
	try:
		artist=Artist.objects.all()
	except Artist.DoesNotExist:
		raise Http404('poll does not exist')
	return render(request,'index.html',{'artist':artist})
