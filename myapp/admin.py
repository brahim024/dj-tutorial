from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_desplay=('title','slug','author','publisher','status')
	list_filter=('status','created','publish','author')
	search_fields=('title','body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
  	

'''
		('Name' ,{'fields':['title']}),


	]'''