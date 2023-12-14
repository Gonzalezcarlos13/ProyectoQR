from django.db import models

# Create your models here.
class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2)
        
    def __str__(self):
        return f"{self.nombre}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2)
        
    def __str__(self):
        return f"{self.nombre}"
    
class Seccion(models.Model):
    profesor = models.ForeignKey(Profesores, null=True,blank=True,on_delete=models.RESTRICT)
    seccion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.seccion}"
        
class Clases(models.Model):
    numero = models.IntegerField()
    seccion = models.ForeignKey(Seccion,null=True,blank=True,on_delete=models.RESTRICT)
    fecha_clase = models.DateField()
    estado = models.CharField(max_length=50, null=True)
    codigo = models.CharField(max_length=100, null=True)
    horario = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Clase N°{self.numero} - Sección: {self.seccion}"
    

class Asistencias(models.Model):
    clases = models.ForeignKey(Clases,null=True,blank=True,on_delete=models.RESTRICT)
    alumno = models.ForeignKey(Alumno, null=True,blank=True,on_delete=models.RESTRICT)
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return f"Clase N°{self.clases.numero} - Alumno: {self.alumno}"
    
class Usuario(models.Model):
    # Puedes agregar campos personalizados aquí si es necesario
    pass