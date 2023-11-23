from django.db import models

# Create your models here.
class Emprendimiento(models.Model):
    nombreProyecto = models.CharField(max_length=50)
    detalleEmprendimiento = models.CharField(max_length=1000)
    imagenEmprendimiento = models.CharField(max_length=250)
    estadoEmprendimiento = models.CharField(max_length=50)