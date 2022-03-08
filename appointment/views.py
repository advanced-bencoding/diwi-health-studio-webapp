from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import EditAppointmentForm

# Create your views here.


def book(request):
    if request.method == "POST":

            a = Appointment()
            a.fname = request.POST['fname']
            a.lname = request.POST['lname']
            a.age = request.POST['age']
            a.date = request.POST['date']

            if '@'and '.' in request.POST['email']:
                a.email = request.POST['email']
            else :
                return render(request,'appointment/book.html',{'wrongmail':'Email is not valid, try again !!'})

            if len(request.POST['mobile'])<10 :
                return render(request,'appointment/book.html',{'wrongno':'Mobile number is not valid , try again!!'})
            else :
                if request.POST['mobile'].startswith('+91'):
                    a.mobile_no = request.POST['mobile']
                else :
                    a.mobile_no = '+91'+request.POST['mobile']

            a.Notes = request.POST['notes']
            a.service = request.POST['service']
            a.sex = request.POST['sex']
            a.slot = request.POST['slot']

            a.save()
            return redirect('/?resp=Appointment Requested Successfuly. We will contact you shortly to confirm your booking.')
    else:
        return render(request, 'appointment/book.html')


@login_required
def manage(request):
    return render(request, 'appointment/manage.html')

@login_required
def view(request):
    clients_confirmed = Appointment.objects
    if request.method=="POST":
        id = request.POST['id']
        client = clients_confirmed.get(pk=id)
        client.delete()
        return redirect('/view/')
    return render(request, 'appointment/view.html', {'clients_confirmed': clients_confirmed})

@login_required
def edit(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.method=="POST":
        appointment.date = request.POST['date']
        appointment.time_start = request.POST['time_start']
        appointment.time_end = request.POST['time_end']
        appointment.save()
        return redirect('/view/')
    form = EditAppointmentForm
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(request, 'appointment/edit.html', {'appointment': appointment, 'form': form,})

@login_required
def create(request):
    if request.method=="POST":
        a = Appointment()
        a.fname = request.POST['fname']
        a.lname = request.POST['lname']
        a.age = request.POST['age']
        a.date = request.POST['date']
        a.Notes = request.POST['notes']
        a.service = request.POST['service']
        a.sex = request.POST['sex']
        a.time_start = request.POST['time_start']
        a.time_end = request.POST['time_end']
        a.mobile_no = request.POST['mobile']
        a.email = request.POST['email']
        a.verified = request.POST['verified']
        a.status = request.POST['verified']
        a.save()
        return redirect('/view/')
    return render(request, 'appointment/create.html')