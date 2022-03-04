from django.db import models


# Create your models here.
class Staff(models.Model):
    image = models.ImageField(upload_to='images/staff/')
    name =  models.CharField(max_length=100)
    qualifications = models.CharField(max_length=50)
