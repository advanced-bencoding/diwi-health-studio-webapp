from django.db import models
from services.models import Services


# Create your models here.
class Staff(models.Model):
    image = models.ImageField(upload_to='images/staff/')
    name =  models.CharField(max_length=100)
    qualifications = models.CharField(max_length=50)
    department = models.ManyToManyField(Services)

    def __str__(self):
        return self.name