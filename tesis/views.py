from django.http import HttpResponse
from django.shortcuts import render, redirect


def homePage(request):
    return redirect(vista1Def)

def vista1Def(request):
    return render(request, 'vista1.html')
