from django.shortcuts import render,redirect, HttpResponse
from .models import *


# Create your views here.

def home(requests):
    return render(requests, 'index.html')
