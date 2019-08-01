from django.db import models
from ..vehicle.models import Vehiculo
from ..customer.models import Cliente
from django.db.models.signals import pre_save, post_save, post_delete


class Factura(models.Model):
    """Informacion de la factura."""


    PAYMENT_CHOICES = [
        ("cs", "cash"),
        ("ca", "card"),
        ("cu", "cupon"),
    ]
    no_factura = models.CharField(max_length=12)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    order = models.OneToOneField("Order", on_delete=models.CASCADE)
    payment = models.CharField(max_length=2, choices=PAYMENT_CHOICES)

    def __str__(self):
        return str(self.order.id)
    
    def total(self):
        return self.order.total

def invoice_post_save_receiver(sender, instance, *args, **kwargs):
    instance.order.update_status("pa")

post_save.connect(invoice_post_save_receiver, sender=Factura)

class Order(models.Model):
    """Orden de los clientes"""

    # TODO: delivery_type: To eat here or carry out

    fecha = models.DateTimeField(auto_now_add=True)
    vehiculo = models.ManyToManyField(Vehiculo)
    estado = models.CharField(max_length=4)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def update_status(self, choice):
        self.status = choice
        self.save()

    def __str__(self):
        return str(self.id)






