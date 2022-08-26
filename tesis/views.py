from django.http import HttpResponse
from django.shortcuts import render
from practicas.models import Usuario

def vista1Def(request):
    return render(request, 'vista1.html')

def practicass(request):

    return render(request, 'busquedaejemplo.html')

def vista2Def (request):

    usuario=Usuario.objects.all()
    
    return render(request, 'vista2.html',{'cantidad':usuario})
    
