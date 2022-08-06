from django.db import models
from distutils.command.upload import upload


class Post(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField(max_length=300)
	image = models.ImageField(upload_to='event_images/')
	date = models.DateTimeField()
