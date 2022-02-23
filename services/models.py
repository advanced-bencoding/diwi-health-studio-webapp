from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField(upload_to='images/') #To show in list of services
    tagline = models.TextField() #Tagline example: We will make your teeth shine brighter than the sun!!!
    banner = models.ImageField(upload_to='images/') #for the homepage banner

    def __str__(self):
        return self.title

class SubService(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/subservices')
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.title