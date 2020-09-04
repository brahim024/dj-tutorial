from django.http import HttpResponse
import datetime
from django.shortcuts import redirect
from .models import Artist
#from .forms import UploadFileForm
#from somewhere import handle_uploaded_file
# Create your views here.
'''def upload_file(request):
	if request.method=='POST':
		form=UploadFileForm(request.POST,request.FILES)
		if request.is_valid():
			handle_uploaded_file(request.FILES['file'])
			return HttpResponseRedirect('succes/url/')
	else:
		form =UploadFileForm()
	return render(request,'index.html',{'forms':form})
	'''
def artist(request):
	obj=Artist.objects.all()
	return redirect('https://github.com/')