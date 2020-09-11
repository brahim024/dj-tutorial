from django.db import models
from django.contrib.auth.models import User

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
class Publisher(models.Model):
	name=models.CharField(max_length=20)
	address=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=20)
	website=models.URLField()
	def __str__(self):
		return self.name
class Author(models.Model):
	salutation=models.CharField(max_length=20)
	name=models.CharField(max_length=20)
	email=models.EmailField()
	headshot=models.ImageField(upload_to='author_headshots')
	def __str__(self):
		return self.name
class Book(models.Model):
	title=models.CharField(max_length=50)
	authers=models.ManyToManyField('Author')
	pubisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	
