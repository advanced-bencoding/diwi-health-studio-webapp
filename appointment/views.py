from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def book(request):
    return render(request, 'appointment/book.html')

@login_required
def manage(request):
    return render(request, 'appointment/manage.html')