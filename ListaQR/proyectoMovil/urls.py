from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='INDEX'),
    path('api/profesores/', listarProfesores, name='LIST_TICHER'),
    path('api/mostrarAsistencias/', listaAsistencia, name='LIST_LIST'),
    path('api/mostrarClases/', listaClases, name='SHOW-CLASSES'),
    path('api/mostrarSecciones/', listarSecciones, name='SHOW_SECCIONS'),
    path('api/comenzarClases/<str:seccion>/<str:horario>/', ingresarClases, name='START_CLASSES'),
    path('registro/', registrar_usuario, name='REG-USE')
    
]