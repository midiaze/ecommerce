from django.db import models
from apps.usuarios.models import Usuario
from apps.productos.models import Producto

# Create your models here.
class Compra(models.Model):
    cliente = models.ForeignKey(Usuario, related_name="compras_cliente", on_delete=models.PROTECT)
    total_compra = models.PositiveIntegerField()
    ruta_boleta = models.CharField(max_length=255, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Pedido(models.Model):
    compra = models.ForeignKey(Compra, related_name="pedido_detalle", on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, related_name="pedidos", on_delete=models.PROTECT)
    cantidad = models.PositiveSmallIntegerField()
    precio_total = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Carrito(models.Model):
    producto = models.ForeignKey(Producto, related_name="carrito_producto", on_delete=models.CASCADE)
    cliente = models.ForeignKey(Usuario, related_name="carrito_cliente", on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

