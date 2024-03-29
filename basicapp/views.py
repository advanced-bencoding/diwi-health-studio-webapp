from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from appointment.models import Appointment
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.POST.get("email")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<gmail id>',[email],fail_silently=False,html_message=htmlgen)
    return HttpResponse(o)

def otp(request):
    if request.method=="POST":
       id = request.POST['id']
       client = Appointment.objects.get(pk=id)
       client.verified = True
       client.save()
    return redirect ('/?resp=Appointment Requested Successfuly. We will contact you shortly to confirm your booking.')
    
