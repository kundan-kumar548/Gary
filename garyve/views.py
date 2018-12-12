from django.shortcuts import render,redirect, HttpResponse
from .models import *


# Create your views here.

def home(request):
    return render(request, 'garyve/garyve_index.html')


def about(request):
    return render(request, 'garyve/garyve_about.html')


def programmer_list(request):
    progrmmer = Programmer.objects.all()
    #value(programmer) in the render is the variable that carry list of all programmer
    #key(programmer) that pass the all the data from database fetch by programmer variable to the html page
    return render(request, 'garyve/programmer.html', {'programmer': progrmmer})


def programmer_detail(request, slug):
    return HttpResponse(slug)