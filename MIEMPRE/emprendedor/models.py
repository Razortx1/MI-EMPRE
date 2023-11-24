from django.db import models

# Create your models here.
class Emprendimiento(models.Model):

    CARGOS = [
        ('Valido' ,'Valido'),
        ('No Valido' ,'No Valido')
    ]


    nombreProyecto = models.CharField(max_length=50)
    detalleEmprendimiento = models.CharField(max_length=1000)
    imagenEmprendimiento = models.ImageField(upload_to="emprendimiento/", null=True)
    estadoEmprendimiento = models.CharField(max_length=50, choices = CARGOS)

def __str__(self):
    return self.name

