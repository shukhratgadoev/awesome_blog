from django.db import models
from distutils.command.upload import upload


class Post(models.Model):
	title = models.CharField(max_length=150)
	text = models.TextField(max_length=300)
	image = models.ImageField(upload_to='event_images/')
	date = models.DateTimeField()

	def get_summary(self):
		return self.text[:70]

	def __str__(self):
		return self.title
