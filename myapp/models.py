from django.db import models

# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField(default=18)
	email=models.EmailField(blank=True)
	job_type=models.CharField(max_length=40)
	bio=models.TextField(blank=True)
	def __str__(self):
		return self.name