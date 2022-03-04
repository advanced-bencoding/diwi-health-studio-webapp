from django.shortcuts import render
from services.models import Services, SubService
from staff.models import Staff
# Create your views here.
def home(request):
    s = Services.objects
    sub = SubService.objects
    staffs = Staff.objects
    return render(request, 'home/home.html', {'s': s, 'sub': sub, 'staffs': staffs,})