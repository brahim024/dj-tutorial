from .models import Product
from .serializers import ProductSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def post_list_api(request):
	all_post=Product.objects.all()
	data=ProductSerializers(all_post,many=True).data
	return Response({'data':data})

@api_view(['GET'])
def post_detail(request,id):
	post_detail=Post.objects.get(id=id)
	data=ProductSerializers(post_detail).data
	return Response({'data':data})