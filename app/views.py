# Create your views here.
from django.shortcuts import render

def home(request):
    c = {'content':'The start of Project Asteria'}
    return render(request, 'home.html', c)
