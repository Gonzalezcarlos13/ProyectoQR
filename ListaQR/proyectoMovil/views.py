from django.shortcuts import redirect, render
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Max
from datetime import datetime
from .models import *

# Create your views here.
def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM proyectomovil_profesores")
        #cursor.execute("SELECT * FROM miapp_tumodelo WHERE edad > %s", [25])
        resultados_sql_directa = cursor.fetchall()
        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]
        # Convertir cada fila en un diccionario
        resultados_dict = [dict(zip(column_names, row)) for row in resultados_sql_directa]
    return render(request, 'index.html', {'profesor': resultados_dict})

def listarProfesores(request):
    try:
        profes = Profesores.objects.all().values()
        return JsonResponse(list(profes), safe=False)
    except Exception as e:
        print(f"Error en la vista listar_profesores: {e}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)
    
def listaAsistencia(request):
    try:
        asistencia = Asistencias.objects.select_related().filter(clases__numero='7').values('clases__numero', 'clases__seccion__seccion', 'clases__fecha_clase', 'clases__estado', 'clases__codigo', 'clases__horario', 'alumno__nombre', 'alumno__apellido', 'alumno__sexo','asistio')
        return JsonResponse(list(asistencia), safe=False)
    except Exception as e:
        print(f"Error en la vista listar_profesores: {e}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)

def listaClases(request):
    try:
        clases = Clases.objects.select_related('seccion').values('numero','estado','fecha_clase', 'codigo')
        return JsonResponse(list(clases), safe=False)
    except Exception as e:
        print(f"Error en la vista listar_profesores: {e}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)
    
def listarSecciones(request):
    try:
        secciones = Seccion.objects.select_related().values('seccion', 'profesor__nombre', 'profesor__apellido')
        return JsonResponse(list(secciones), safe=False)
    except Exception as e:
        print(f"Error en la vista listar_profesores: {e}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)

def ingresarClases(request, seccion, horario):
    try:
        seccion_existente = Seccion.objects.get(seccion=seccion)
        ultimo_numero_clase = Clases.objects.filter(seccion=seccion_existente).aggregate(Max('numero'))['numero__max']
        nuevo_numero_clase = ultimo_numero_clase + 1 if ultimo_numero_clase is not None else 1
        fecha_actual = datetime.now().strftime('%Y-%m-%d')

        clases = Clases(
            numero=str(nuevo_numero_clase),
            seccion=seccion_existente,
            fecha_clase=fecha_actual,
            estado='Iniciada',
            codigo= "CLASE" + str(nuevo_numero_clase) + "/" + seccion + "/" + fecha_actual,
            horario=horario
        )
        clases.save()
        
        clase_seleccionada = Clases.objects.get(numero=clases.numero)
        
        alumnos = Alumno.objects.all()
        
        for alumnoo in alumnos:
            asistencias = Asistencias(
                clases = clase_seleccionada,
                alumno = alumnoo,
                asistio = False
            )
            asistencias.save()
            
        return JsonResponse({"mensaje": "La clase se ha ingresado de forma exitosa con el código: " + clases.codigo})
    except Exception as e:
        print(f"Error al ingresar clases: {e}")
        return JsonResponse({"error": "Error interno del servidor"}, status=500)

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect('ruta_exitosa')  # Puedes redirigir a la página que desees después del registro
    else:
        form = UserCreationForm()

    return render(request, 'registro_usuario.html', {'form': form})#/