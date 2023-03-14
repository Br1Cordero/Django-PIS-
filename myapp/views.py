from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def Hello(request):
    return render(request,'index.html')

def Votar(request):
    return render(request,'votacion.html')

def Estadisticas(request):
    return render(request,'estadisticas.html')
