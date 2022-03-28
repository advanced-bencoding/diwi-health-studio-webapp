from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import EditAppointmentForm
from django.core.mail import send_mail,EmailMessage
from diwihealthstudio import settings
from services.models import Services

sender = settings.EMAIL_HOST_USER

# Create your views here.


def book(request):
    if request.method == "POST":
        a = Appointment()
        a.fname = request.POST['fname']
        a.lname = request.POST['lname']
        a.age = request.POST['age']
        a.date = request.POST['date']
        
        if '@' and '.' in request.POST['email']:
            a.email = request.POST['email']
            mail=request.POST['email']
        else:
            return render(request, 'appointment/book.html', {'wrongmail': 'Email is not valid, try again !!'})

        if (request.POST['mobile']).isdigit():
            if len(request.POST['mobile']) == 10:
                a.mobile_no = '+91' + request.POST['mobile']
            else:
                return render(request, 'appointment/book.html', {'wrongmno': 'Invalid mobile number, try again!!'})

        elif len(request.POST['mobile']) == 13:
            if request.POST['mobile'].startswith('+91'):
                if request.POST['mobile'][1:12].isdigit():
                    a.mobile_no = request.POST['mobile']
            else:
                return render(request, 'appointment/book.html', {'wrongmno': 'Invalid mobile number, try again!!'})

        a.Notes = request.POST['notes']
        a.service = Services.objects.get(id=request.POST['service'])
        a.sex = request.POST['sex']
        a.slot = request.POST['slot']

        a.save()
       # return redirect('/?resp=Appointment Requested Successfuly. We will contact you shortly to confirm your booking.')
        return render(request,'basicapp/home.html',{'id':a.id,'email':mail} )
    else:
        services = Services.objects.all()
        return render(request, 'appointment/book.html', {'services': services})


@login_required
def manage(request):
    if request.method=="POST":      
            id = request.POST['id']
            appointment = Appointment.objects.get(pk=id)
            if request.POST['action'] == "Confirm":
                appointment.date = request.POST['date']
                appointment.time_start = request.POST['time_start']
                appointment.time_end = request.POST['time_end']
                appointment.status = 't'

                email = appointment.email
                
                appointment.save()
                message = 'Your Appointment for ' + str(appointment.service) +' is Successfully booked .'+ ' Your appointment is scheduled on Date '+appointment.date+' from ' +appointment.time_start+ ' to '+appointment.time_end+'.'

                
                
                send_mail(
                            'Appointment Booked' , #subject
                            message, #message
                            sender, #from email
                            [email], #to email
                            fail_silently= False,

                            )
                return redirect('/manage/?resp=Appointment Confirmed Successfully.')
            elif request.POST['action'] == "Reject":
                # date1 = (str)appointment.date
                email = appointment.email
                message = 'Your appointment for '+appointment.service+' on '+str(appointment.date)+ '  is cancelled.'
                send_mail(
                'Appointment Cancelled' , #subject
                    message, #message
                    sender, #from email
                    [email], #to email
                    fail_silently= False,

                    )

                appointment.delete()


                return redirect('/manage/?resp=Appointment Request Deleted.')
    b = Appointment.objects.filter(verified=True,status=False).order_by('date', 'time_start')
    message = request.GET.get('resp')
    return render(request, 'appointment/manage.html',{'aps':b, 'message':message})


@login_required
def view(request):
    clients_confirmed = Appointment.objects.all().order_by('date', 'time_start')
    if request.method == "POST":
        id = request.POST['id']
        client = clients_confirmed.get(pk=id)
        if request.POST['sub'] == "Cancel Appointment":
            email = client.email
            message = 'Your appointment for '+str(client.service)+' on '+str(client.date)+'is cancelled.'
            send_mail(
                'Appointment Cancelled' , #subject
                message, #message
                sender, #from email
                [email], #to email
                fail_silently= False,

                )
        client.delete()
        return redirect('/view/')
    return render(request, 'appointment/view.html', {'clients_confirmed': clients_confirmed})


@login_required
def edit(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)
    if request.method == "POST":
        appointment.date = request.POST['date']
        appointment.time_start = request.POST['time_start']
        appointment.time_end = request.POST['time_end']

        email = appointment.email
        message = ' Your Appointment for '+str(appointment.service)+' has been rescheduled. New date: ' +str(appointment.date)+'. New time slot: ' + appointment.time_start+ ' to ' +appointment.time_end + '.'

        send_mail(
            'Appointment Rescheduled' , #subject
            message, #message
            sender, #from email
            [email], #to email
            fail_silently= False,

            )

        appointment.save()


        return redirect('/view/')
    form = EditAppointmentForm
    appointment = Appointment.objects.get(pk=appointment_id)
    return render(request, 'appointment/edit.html', {'appointment': appointment, 'form': form, })


@login_required
def create(request):
    if request.method == "POST":
        a = Appointment()
        a.fname = request.POST['fname']
        a.lname = request.POST['lname']
        a.age = request.POST['age']
        a.date = request.POST['date']
        a.Notes = request.POST['notes']
        a.service = Services.objects.get(id=request.POST['service'])
        a.sex = request.POST['sex']
        a.time_start = request.POST['time_start']
        a.time_end = request.POST['time_end']
        a.mobile_no = request.POST['mobile']
        a.email = request.POST['email']
        a.verified = request.POST['verified']
        a.status = request.POST['verified']

        email = a.email
        message = 'Your Appointment for ' + str(a.service) +' is Successfully booked .'+ ' Your appointment is scheduled on Date '+a.date+' from ' +a.time_start+ ' to '+a.time_end+'.'
        send_mail(
                            'Appointment Booked' , #subject
                            message, #message
                            sender, #from email
                            [email], #to email
                            fail_silently= False,

                            )

        a.save()
        return redirect('/view/')
    services = Services.objects.all()
    return render(request, 'appointment/create.html', {'services': services})

def confirm():
    {
        
}