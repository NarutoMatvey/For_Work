from django.db import models

# Create your models here.
class Episodes(models.Model):
	title_episod = models.CharField(max_length=120)
	description_episode = models.TextField()
	release_episode = models.DateTimeField('date release')