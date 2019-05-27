from django.db import models
from django.db.models import CharField

# Create your models here.
class Order(models.Model):
    cancel = models.CharField(max_length=200)
    new = models.CharField(max_length=200)
    shipped = models.CharField(max_length=200)
    processing = models.CharField(max_length=200)
