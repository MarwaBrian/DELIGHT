from django.shortcuts import render
from .models import Caakes

from django.http import HttpResponse


cakes = [
    {
    'cake_type': 'Vanilla',
    'availability': '300',
    'Best_Before': 'Today',
    #remember to render instock instead of true and false
    #i fixed the render by introducing an 'if' conditional in the cakes.html file
    'in_stock' : 'IN STOCK',
    },
     {
    'cake_type': 'Pinacolada',
    'availability': 'In Stock',
    'Best_Before': 'Today',
    },
]


def home(request):
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/delight_Cakehouse/templates/delight_Cakehouse/home.html")

def Cakes(request):
    content = {
        'cakes': Caakes.objects.all
    }
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/delight_Cakehouse/templates/delight_Cakehouse/cake.html", content)

def Cookie(request):
    return render(request, "/home/marwa254/Desktop/DELIGHT/mysite/delight_Cakehouse/templates/delight_Cakehouse/cookie.html")