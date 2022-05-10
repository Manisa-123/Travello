from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    off = models.BooleanField(default=False)

    