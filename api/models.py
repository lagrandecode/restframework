
from django.db import models

# Create your models here.

class Api(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

