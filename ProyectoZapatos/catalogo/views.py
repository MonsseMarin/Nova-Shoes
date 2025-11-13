from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def catalogo(request):
    return render(request, 'catalogo/catalogo.html')