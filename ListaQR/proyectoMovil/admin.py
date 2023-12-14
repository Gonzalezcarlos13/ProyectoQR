from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profesores)
admin.site.register(Seccion)
admin.site.register(Clases)
admin.site.register(Asistencias)
admin.site.register(Alumno)