from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import *
from AppEscuela.forms import *

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

#Clase 19 con Franco 11:17
def inicio (request):
    return render (request,"inicio.html")
    
def materiasformulario (request):
    
    if request.method=="POST":
        form=MateriasForm (request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            
            nombre=informacion ["nombre"]
            curriculum=informacion ["curriculum"]
            ano_dictado=informacion ["ano_dictado"]
          
            materia= Materias(nombre=nombre, curriculum=curriculum, ano_dictado=ano_dictado)
            materia.save()
            return render (request,"inicio.html", {"mensaje":"Materia Creada!"})
    else:
        formulario=MateriasForm() 
    
    
    return render (request, "materiasformulario.html", {"form":formulario} )

#alumnosForm

def alumnosformulario (request):
    
    if request.method=="POST":
        form=AlumnosForm (request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            
            nombre=informacion ["nombre"]
            apellido=informacion  ["apellido"]
            edad=informacion ["apellido"]
            modalidad=informacion ["modalidad"]
            
            alumno= Alumno(nombre=nombre, apellido=apellido, edad=edad, modalidad=modalidad)
            alumno.save()
            return render (request,"inicio.html", {"mensaje":"Alumno Creado!"})
    else:
        formulario=AlumnosForm() 
    
    
    return render (request, "alumnosformulario.html", {"form":formulario} )

def profesoresformulario (request):
    
    if request.method=="POST":
        form=ProfesoresForm (request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            
            nombre=informacion ["nombre"]
            apellido=informacion  ["apellido"]
            antiguedad=informacion ["antiguedad"]
            asignatura=informacion ["asignatura"]
            
            profesor= Profesores(nombre=nombre, apellido=apellido, antiguedad=antiguedad, asignatura=asignatura)
            profesor.save()
            return render (request,"inicio.html",{"mensaje":"Profesor Creado!"} )
    else:
        formulario=ProfesoresForm() 
    
    
    return render (request, "profesoresformulario.html", {"form":formulario} )

def busquedaprofesores(request):
    return render (request, "busquedaprofesores.html")

def busquedaalumnos(request):
    return render (request, "busquedaalumnos.html")

def busquedamaterias(request):
    return render (request, "busquedamaterias.html")

def buscar(request):
    
    if request.GET ["antiguedad"]:
        
        antiguedad=request.GET ["antiguedad"]
        
        profesores=Profesores.objects.filter(antiguedad=antiguedad)
        return render (request,"resultadosbusqueda.html", {"profesores":profesores} )
    else:
        return render (request, "busquedaprofesores.html", {"mensaje":"Ingresa la antiguedad"})
    


