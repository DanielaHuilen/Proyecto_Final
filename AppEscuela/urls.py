from django.urls import path
from AppEscuela import views

urlpatterns = [
    path ('', views.Profesores_index, name='profesores.index'),
    path ('/nuevo', views.Profesores_form, name='profesores.form'),
    path ('/busqueda', views.Profesores_search, name='profesores.search'),
    
]
