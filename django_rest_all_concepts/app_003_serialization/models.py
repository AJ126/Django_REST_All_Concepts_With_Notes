from django.db import models

# Create your models here.
class detail(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)