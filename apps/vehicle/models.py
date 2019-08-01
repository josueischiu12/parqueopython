from django.db import models



class VehiculoTipo(models.Model):
    nombre = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    Vehiculo_tipo = models.ForeignKey(VehiculoTipo, on_delete = models.PROTECT)
    plate = models.CharField(max_length=10)
    color = models.TextField(max_length=10)

    def __str__(self):
        return self.plate


    
