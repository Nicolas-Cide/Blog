from django.db import models

# Create your models here.

class familiaPrinc(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNac = models.DateField()

    def __str__(self):
        return f'El nombre y apellido es: {self.nombre} {self.apellido}. Edad: {self.edad}, Fecha de nacimiento {self.fechaNac} '




class familiaSec(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaNac = models.DateField()