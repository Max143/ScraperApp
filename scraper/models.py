from django.db import models


class Blogs(models.Model):
	headline = models.CharField(max_length=300, blank=True,  primary_key=True)
	summary = models.TextField(blank=True)
	category = models.CharField(max_length=100, blank=True)
	link = models.URLField(blank=True)

	def __str__(self):
		return self.headline + " | " + self.category