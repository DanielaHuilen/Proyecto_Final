from django.db import models

# Create your models here.

class Profesores (models.Model):
    nombre= models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    antiguedad=models.IntegerField()
    asignatura=models.CharField(max_length=20)
    
    def __str__ (self):
        return f"Docente: {self.apellido} {self.nombre}, docente de {self.asignatura} "
    
class Alumno (models.Model):
    nombre= models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    edad=models.IntegerField()
    
    def __str__ (self):
        return f"Alumno: {self.apellido} {self.nombre}"
    
class Materias (models.Model):
    nombre= models.CharField(max_length=20)
    curriculum=models.URLField()
    ano_dictado=models.IntegerField()

    
    def __str__ (self):
        return f"Materia: {self.nombre}, curriculum: {self.curriculum}"
    
