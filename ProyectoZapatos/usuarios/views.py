from django.shortcuts import render

# Create your views here.
def usuarios(request):
    return render(request, 'usuarios/usuarios.html')

def registro(request):
    return render(request, 'usuarios/registro.html')