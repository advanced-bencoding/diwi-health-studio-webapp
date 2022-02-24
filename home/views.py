from django.shortcuts import render
from services.models import Services, SubService
# Create your views here.
def home(request):
    s = Services.objects
    sub = SubService.objects
    return render(request, 'home/home.html', {'s': s, 'sub': sub})