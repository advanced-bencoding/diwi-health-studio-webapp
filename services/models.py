from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/')
    tagline = models.TextField() #Tagline example: We will make your teeth shine brighter than the sun!!!