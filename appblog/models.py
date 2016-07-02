from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Post (models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey('auth.user')
	publish_date = models.DateTimeField(default=timezone.now())
	
	def publish(self):

		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title