from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import *

# Create your views here.
def Profesores_index (request:HttpRequest) -> HttpResponse:
    profesores= Profesores.objects.all()
    return render (request, 'profesores_index.html', {"profesores":profesores})

def alumnos_index (request:HttpRequest) -> HttpResponse:
    alumnos= Alumno.objects.all()
    return render (request, 'alumnos_index.html', {"alumnos":alumnos})


def materias_index (request:HttpRequest) -> HttpResponse:
    materias= Materias.objects.all()
    return render (request, 'materias_index.html', {"materias":materias})

