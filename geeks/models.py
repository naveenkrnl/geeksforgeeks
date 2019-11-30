from django.db import models
from django.utils.text import slugify 

# Create your models here.
class GeeksModel(models.Model):
	title=models.CharField(max_length=200)
	img=models.ImageField(upload_to="images/")

	def __str__(self):
		return self.title