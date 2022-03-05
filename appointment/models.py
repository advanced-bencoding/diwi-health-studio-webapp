from django.db import models

# Create your models here.
class Appointment (models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    date = models.DateTimeField()
    time = models.CharField(max_length=100)
    Notes = models.TextField()
    service = models.CharField(max_length=20)

    def __str__(self) :
        return self.fname + self.lname
