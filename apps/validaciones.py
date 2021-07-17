from django.core.exceptions import ValidationError

def longitud(campo, cadena, minimo = 2, maximo = 20):
    if len(cadena)<minimo:
        raise ValidationError(f"El {campo} no puede ser menor de {minimo} caracteres.")
    if len(cadena)>maximo:
        raise ValidationError(f"El {campo} no puede ser mayor de {maximo} caracteres.")