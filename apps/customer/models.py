from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    """Informacion del cliente."""

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    tax_id = models.TextField(blank=True, default="C/F")
    direccion = models.TextField(blank=True, default="Ciudad")
    telefono = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

