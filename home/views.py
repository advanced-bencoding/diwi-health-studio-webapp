from django.shortcuts import render
from services.models import Services
# Create your views here.
def home(request):
    s = Services.objects
    return render(request, 'home/home.html', {'s': s})