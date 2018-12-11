from django.shortcuts import render,redirect, HttpResponse
from .models import *


# Create your views here.

def home(requests):
    return render(requests, 'index.html')


def about(requests):
    return render(requests, 'about.html')


def about_gary(requests):
    return render(requests, 'garyve/garyve_about.html')

