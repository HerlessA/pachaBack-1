from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Biography(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_nacimiento = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(blank=True,null=True)
    nacionalidad = models.ForeignKey('biography.Nationality',on_delete=models.CASCADE)
    religiion = models.CharField(max_length=200)
    educacion = models.TextField()
    ocupacion = models.TextField(max_length=200)
    empleador = models.TextField(max_length=200)
    sitio_web = models.CharField(max_length=200)

    def __str__(self):
        return str(self.nombre_nacimiento)
    

class Nationality(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_pais