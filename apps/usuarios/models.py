from django.db import models
from apps.productos.models import Producto

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    super_user = models.BooleanField(default=False)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    es_activo = models.BooleanField(default=True)
    carrito = models.ManyToManyField(Producto, through='pedidos.Carrito')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


