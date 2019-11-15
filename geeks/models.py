from django.db import models
from django.utils.text import slugify 

# Create your models here.
class GeeksModel(models.Model):
	title=models.CharField(max_length=200)
	slug=models.SlugField()

	def save(self,*args,**kwargs):
		self.slug=slugify(self.title)
		super(GeeksModel,self).save(*args,**kwargs)
