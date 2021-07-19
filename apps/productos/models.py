from django.db import models

# Create your models here.
class ProductoManager(models.Manager):
    
    def validar_edicion(self, post_data):
        errors = {}
        if len(post_data['nombre'])<2:
            errors['nombre'] = 'Nombre debe tener al menos dos caracteres'
        if int(post_data['precio']) <= 0:
            errors['precio'] = 'Precio no puede ser cero'
        if len(post_data['descripcion'])<2:
            errors['descripcion'] = 'Descripción debe tener al menos dos caracteres'
        if int(post_data['stock']) < 0:
            errors['stock'] = 'Stock no puede ser menor a cero'
        if int(post_data['min_stock']) < 0:
            errors['min_stock'] = 'Stock no puede ser menor a cero'

        return errors


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

    objects = ProductoManager()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['created_at']
