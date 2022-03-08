from django.db import models

# Create your models here.
class Appointment (models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=13)
    email = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    Notes = models.TextField(null=True)
    service = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    slot = models.CharField(max_length=10, default="Morning")

    def __str__(self) :
        return self.fname + self.lname