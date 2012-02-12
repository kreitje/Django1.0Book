from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
	url = models.URLField(unique=True)
	
class Bookmark(models.Model):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	link = models.ForeignKey(Link)
