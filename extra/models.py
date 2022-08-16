from django.db import models
from accounts.models import UserModel
from content.models import PostModel

class TagModel(models.Model):
	# users = models.ManyToManyField()
	posts = models.ManyToManyField(PostModel, blank=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name
