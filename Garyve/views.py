from django.shortcuts import render,redirect, HttpResponse


# Create your views here.

def home(requests):
    return render(requests, 'index.html')
