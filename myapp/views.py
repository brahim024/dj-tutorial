from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UploadFileForm
from somewhere import handle_uploaded_file
# Create your views here.
def upload_file(request):
	if request.method=='POST':
		form=UploadFileForm(request.POST,request.FILES)
		if request.is_valid():
			handle_uploaded_file(request>FILES['file'])
	else:
		form =UploadFileForm()
	return render(request,'upload.html',{'forms':form})