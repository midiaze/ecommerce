from django import forms
from django.forms import fields, widgets
from apps.usuarios.models import Usuario
import apps.validaciones as validar
from django.core.exceptions import ValidationError

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['nombre', 'direccion', 'email', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }
    
        error_messages = {
            'nombre': validar.mensajes_error_por_defecto,
            'direccion': validar.mensajes_error_por_defecto,
            'email': validar.mensajes_error_por_defecto,
            'password': validar.mensajes_error_por_defecto,
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        validar.longitud("nombre", nombre)
        return nombre
    
    def clean_direccion(self):
        direccion = self.cleaned_data['direccion']
        validar.longitud("direccion", direccion)
        return direccion
    
    def clean_password(self):
        password = self.cleaned_data['password']
        validar.longitud("password", password, minimo=6)
        return password
    
    