from django.views.generic import CreateView
from django.shortcuts import render
from .models import Person
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
	return render(request,'index.html',{'forms':form})'''
class PersonCreateView(CreateView):
	model = Person
	template_name='person_form.html'
	fields = ('name','age','job_type','bio')