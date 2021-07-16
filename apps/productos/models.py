from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    precio = models.PositiveIntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to = 'productos', default="blanco.jpg")
    stock = models.PositiveIntegerField(blank=True, null=True)
    min_stock = models.PositiveIntegerField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
