from django.shortcuts import render
from services.models import Services
from services.models import SubService
# Create your views here.
def services(request):
    s = Services.objects.all()
    sub = SubService.objects.all()
    return render(request, 'services/services.html', {'s':s, 'sub':sub})