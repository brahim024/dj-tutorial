from django.shortcuts import render , redirect , reverse
from .models import Product
from django .http import Http404
def product(request,id):
	products=Product.objects.get(id=id)
	return render(request,'index.html',{'products':products})
def like_deslike(request,id):
	products=Product.objects.get(id=id)
	if request.user in products.like.all():
		products.like.remove(request.user)
	else:
		products.like.add(request.user)
	return redirect(reverse('detail',kwargs={'id':products.id}))
def user_favorite(request):
	user_favorite=Product.objects.filter(like=request.user)
	return render (request,'person_form.html',{'user_favorite':user_favorite})


