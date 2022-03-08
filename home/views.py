from email import message
from django.shortcuts import render
from services.models import Services, SubService
from staff.models import Staff
# Create your views here.
def home(request):
    message = request.GET.get('resp')
    s = Services.objects
    sub = SubService.objects
    staffs = Staff.objects
    return render(request, 'home/home.html', {'s': s, 'sub': sub, 'staffs': staffs, 'message': message})