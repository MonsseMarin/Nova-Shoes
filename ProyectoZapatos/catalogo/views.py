from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def catalogo(request):
    return render(request, 'catalogo/catalogo.html')

def catalogo_mujer(request):
    return render(request, 'catalogo/catalogomujer.html')

def catalogo_hombre(request):
    return render(request, 'catalogo/catalogohombre.html')

def catalogo_ninos(request):
    return render(request, 'catalogo/catalogoninos.html')