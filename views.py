from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, 'AppRegistro/inicio.html')

# def personas(request):

#     return render(request, 'Appcoder/personas.html')

def usuario(request):

    return render(request, 'AppRegistro/usuario.html') 

def pedido (request):

    return render(request, 'AppRegistro/pedido.html')

