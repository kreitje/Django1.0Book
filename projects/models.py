from django.db import models

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=50)
	description = models.CharField(max_length=200)
	long_description = models.TextField()
	date_created = models.DateTimeField('date created')
	status = models.BooleanField()
	
class Tasks(models.Model)
	project = models.ForeignKey(Project)
	subject = models.CharField(max_length = 200)
	task = models.TextField()
	date_created = models.DateTimeField('date created')
	date_closed = models.DateTimeField('date closed')