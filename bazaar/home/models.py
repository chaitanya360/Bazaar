from django.db import models
import datetime
# Create your models here.


class electronics(models.Model):
    image = models.ImageField(upload_to ='uploads/%Y/%m/%d/')
    title = models.CharField(max_length=20)
    specs = models.CharField(max_length=20)



class carousel(models.Model):
    image = models.ImageField(upload_to ='uploads/carousel')
    number = models.IntegerField()