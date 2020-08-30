from django.shortcuts import render
from .models import Artist
# Create your views here.
def artists(request):
	artist=Artist.objects.all()
	return render(request,'index.html',{'artist':artist})