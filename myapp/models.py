from django.db import models

# Create your models here.
class Artist(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField(default=18)
	def __str__(self):
		return self.name