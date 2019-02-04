from django.db import models

# Create your models here.
class PageURL(models.Model):

	url = models.URLField(max_length=250)
	short_url = models.URLField(max_length=50)
