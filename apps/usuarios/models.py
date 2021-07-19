from django.db import models
from apps.productos.models import Producto
import re
import bcrypt



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UsuarioManager(models.Manager):

    def validar_ingreso(self, post_data):
        errors = {}
        if len(post_data['email']) < 1:
            errors['login'] = 'Email es necesario'
        elif not EMAIL_REGEX.match(post_data['email']):
            errors['login']= "Email no es válido"
        else:
            email_existente = Usuario.objects.filter(email=post_data['email'])
            if len(email_existente) == 0:
                errors['login'] = 'Correo y contraseña no coinciden'
            else:
                usuario = email_existente[0]
                if post_data['password'] != usuario.password:
                    errors['login'] = 'Correo y contraseña no coinciden'
        return errors


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    super_user = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    es_activo = models.BooleanField(default=True)
    # carrito = models.ManyToManyField(Producto, through='pedidos.Carrito')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()


