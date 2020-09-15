from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
'''class Person(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField(default=18)
	email=models.EmailField(blank=True)
	job_type=models.CharField(max_length=40)
	bio=models.TextField(blank=True)
	def __str__(self):
		return self.name
class Person(models.Model):
	name=models.CharField(max_length=20)
	age=models.PositiveIntegerField()
	class Meta:
		abstract=True'''
def author_headshots(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,
			self).get_queryset()\
				.filter(status='published')


			

class Post(models.Model):
	STATUS_CHOICES = (
	('draft', 'Draft'),
	('published', 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,
	choices=STATUS_CHOICES,
	default='draft')
	objects=models.Manager()
	published=models.PublishedManager()
	def __str__(self):
 		return self.title
class Meta:
	ordering = ('-publish',)
