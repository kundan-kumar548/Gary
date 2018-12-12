from django.shortcuts import render,redirect, HttpResponse
from .models import *


def home(request):
    return render(request,'garyve/index.html')