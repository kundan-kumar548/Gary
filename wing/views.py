from django.shortcuts import render,redirect, HttpResponse
from .models import *


def home(request):
    grocery = Grocery.objects.all()
    fruit = Fruit.objects.all()
    vegetable = Vegetable.objects.all()
    extras = Extras.objects.all()
    return render(request, 'wing/gallery.html', {'grocery': grocery,
                                                 'fruit': fruit,
                                                 'vegetable': vegetable,
                                                 'extras': extras})
