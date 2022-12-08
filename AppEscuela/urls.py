from django.urls import path
from AppEscuela import views

urlpatterns = [
    
    path ("", views.inicio, name='inicio'), #modificado con clase 19
    path ("profesores", views.Profesores_index, name='profesores_index'),
    #path ('/nuevo', views.Profesores_form, name='profesores-form'),
    #path ('/busqueda', views.Profesores_search, name='profesores-search'),
    path("alumnos", views.alumnos_index, name='alumnos_index'),
    path("materias", views.materias_index, name='materias_index'),
    
]
