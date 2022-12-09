from django import forms 


class MateriasForm (forms.Form):
    nombre= forms.CharField(max_length=50)
    curriculum=forms.URLField()
    ano_dictado=forms.IntegerField()
    
class AlumnosForm (forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    edad=forms.IntegerField()
    modalidad=forms.CharField(max_length=20)
    
class ProfesoresForm (forms.Form):
    nombre= forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    antiguedad=forms.IntegerField()
    asignatura=forms.CharField(max_length=20)
    