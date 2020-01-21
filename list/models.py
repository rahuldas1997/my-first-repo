from django.db import models

# Create your models here.
class details(models.Model):
	FirstName = models.CharField(max_length=30)
	LastName = models.CharField(max_length=30)
	age = models.IntegerField()
	address = models.CharField(max_length=500)
	email = models.EmailField(max_length=250)
	