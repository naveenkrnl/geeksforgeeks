import uuid
from django.db import models

# Create your models here.
class GeeksModel(models.Model):
	geeks_field=models.CharField(max_length=200)