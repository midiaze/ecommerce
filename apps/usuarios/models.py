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
                if not bcrypt.checkpw(post_data['password'].encode(), usuario.password.encode()):
                    errors['login'] = 'Correo y contraseña no coinciden'
                if not usuario.es_activo:
                    errors['login'] = 'Esta cuenta fue eliminada'
        return errors
    
    def validar_editar_usuario(self, post_data):
        errors = {}
        if len(post_data['nombre'])<2:
            errors['nombre'] = 'Nombre debe tener al menos dos caracteres'
        if len(post_data['direccion'])<2:
            errors['direccion'] = 'Apellido debe tener al menos dos caracteres'
        if post_data['email']:
            if not EMAIL_REGEX.match(post_data['email']):
                errors['email']= "Email no es válido"
        return errors
    
    def validar_cambio_pw(self, post_data):
        errors = {}
        if len(post_data['nueva_pw'])<6:
            errors['cambio_pw'] = 'Contraseña debe tener al menos 6 caracteres'
        if post_data['nueva_pw'] != post_data['confirm_nueva_pw']:
            errors['cambio_pw'] = 'Contraseñas no coinciden'
        return errors


class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    super_user = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    es_activo = models.BooleanField(default=True)
    carrito = models.ManyToManyField(Producto, through='pedidos.Carrito')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

