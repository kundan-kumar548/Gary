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


def info(request):
    gro = Grocery.objects.all()
    veg = Vegetable.objects.all()
    fru = Fruit.objects.all()
    extras = Extras.objects.all()
    return render(request, 'wing/item_detail.html', {'grocery': gro,
                                                     'fruit': fru,
                                                     'vegetable': veg,
                                                     'extras': extras})
