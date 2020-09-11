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
class Product(models.Model):
	name=models.CharField(max_length=20)
	image=models.ImageField('img')
	like=models.ManyToManyField(User,blank=True)

	def __str__(self):
		return self.name
