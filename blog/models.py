from distutils.command.upload import upload
from email.mime import image
from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to='images/blog/')
    
    def __str__(self):
        return self.title

