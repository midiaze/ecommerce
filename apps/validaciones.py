from django.core.exceptions import ValidationError

def longitud(campo, cadena, minimo = 2, maximo = 20):
    if len(cadena)<minimo:
        raise ValidationError(f"El {campo} no puede ser menor de {minimo} caracteres.")
    if len(cadena)>maximo:
        raise ValidationError(f"El {campo} no puede ser mayor de {maximo} caracteres.")

mensajes_error_por_defecto = {
    'required': 'Este campo es requerido.',
    'invalid': 'Debe ingresar un valor válido.',
    'min_length': '',
    'wrong_data': 'Los datos ingresados no son correctos',
    # 'unique': 'you enetered in not unique',
    # 'blanck': 'you enetered in not blanck',
    # 'null': 'you enetered in not null',
}