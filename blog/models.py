from distutils.command.upload import upload
from email.mime import image
from django.db import models
from staff.models import Staff
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateField()
    image=models.ImageField(upload_to='images/blog/')
    written_by= models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

