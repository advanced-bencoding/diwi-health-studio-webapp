from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment

# Create your views here.


def book(request):
    if request.method == "POST":
        if request.POST['fname'] and request.POST['lname'] and request.POST['age'] and request.POST['sex'] and request.POST['mobile'] and request.POST['email'] and request.POST['date'] and request.POST['service'] and request.POST['time'] :
            a = Appointment()
            a.fname = request.POST['fname']
            a.lname = request.POST['lname']
            a.age = request.POST['age']
            a.date = request.POST['date']

            if '@'and '.' in request.POST['email']:
                a.email = request.POST['email']
            else :
                return render(request,'appointment/book.html',{'wrongmail':'Email is not valid, try again !!'})

            if request.POST['mobile'].length<10 :
                return render(request,'appointment/book.html',{'wrongno':'Mobile number is not valid , try again!!'})
            else :
                if request.POST['mobile'].startswith('+91'):
                    a.mobile_no = request.POST['mobile']
                else :
                    a.mobile_no = '+91'+request.POST['mobile']

            a.Notes = request.POST['notes']
            a.service = request.POST['service']
            a.sex = request.POST['sex']
            a.time = request.POST['time']

            a.save()
            return render(request,'home/home.html',{'message':'Appointment Booked Successfully'})
    else:
        return render(request, 'appointment/book.html')


@login_required
def manage(request):
    return render(request, 'appointment/manage.html')

@login_required
def view(request):
    return render(request, 'appointment/view.html')