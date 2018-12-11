from django.shortcuts import render,redirect, HttpResponse
from .models import *


# Create your views here.

def home(requests):
    return render(requests, 'garyve/garyve_index.html')


def about(requests):
    return render(requests, 'garyve/garyve_about.html')


def programmer_list(requests):
    progrmmer = Programmer.objects.all()
    #value(programmer) in the render is the variable that carry list of all programmer
    #key(programmer) that pass the all the data from database fetch by programmer variable to the html page
    return render(requests, 'garyve/programmer.html', {'programmer': progrmmer})


def show_list(requests):
    pass