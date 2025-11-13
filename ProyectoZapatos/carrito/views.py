from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def carrito(request):
    return render(request, 'carrito/carrito.html')