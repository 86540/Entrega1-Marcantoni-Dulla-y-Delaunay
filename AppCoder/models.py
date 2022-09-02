from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()
    def __str__(self):
        return self.nombre+' '+str(self.comision)

class Estudiantes(models.Model):
    nombre=models.CharField(max_length=50)
    nota=models.IntegerField()
    email=models.EmailField()
    entregable=models.BooleanField()

class profesores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    profesion=models.CharField(max_length=50)


