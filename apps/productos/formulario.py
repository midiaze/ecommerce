from django import forms
from django.forms import fields, widgets
from apps.productos.models import Categoria, Producto
import apps.validaciones as validar
from django.core.exceptions import ValidationError

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

        error_messages = {
            'nombre': validar.mensajes_error_por_defecto,
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        validar.longitud("nombre", nombre)
        return nombre

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

        error_messages = {
            'nombre': validar.mensajes_error_por_defecto,
            'precio': validar.mensajes_error_por_defecto,
            'descripcion': validar.mensajes_error_por_defecto,
            'categoria': validar.mensajes_error_por_defecto,
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        validar.longitud("nombre", nombre)
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio == 0:
            raise ValidationError(f"El precio no puede ser cero")
        return precio