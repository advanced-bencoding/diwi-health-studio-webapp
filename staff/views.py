from django.shortcuts import render
from.models import Staff

def staff(request):
    staff = Staff.objects
    return render (request,'staff/staff.html',{'workingforce':staff})
