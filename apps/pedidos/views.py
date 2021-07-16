from re import template
from django.shortcuts import redirect, render
from .models import *
from apps.productos.models import Producto
from apps.usuarios.models import Usuario
from pathlib import Path
from django.template.loader import get_template
import os
from django.conf import settings
# from weasyprint import HTML
from apps.utils import login_required


def index(request):
    productos = Producto.objects.all()
    if request.method == 'GET':
        context = {
            'productos': productos
        }
        return render(request, 'home.html', context)


# def boleta(request, pedido_id):
#     pedido = Pedido.objects.get(id=pedido_id)
#     context={            
#         'pedido': pedido
#         }
#     Path('static/pdf').mkdir(parents=True, exist_ok=True)
#     nombreArchivo = f'boleta_{pedido.id}'
#     template = get_template(f'boleta_{pedido.id}.html')
#     html_template = template.render(context)
#     pdf_url = os.path.join(settings.BASE_DIR, 'static/pdf/'+nombreArchivo)
#     HTML(string = html_template).write_pdf(target=f'{pdf_url}.pdf')
#     return render(request, 'paginas/boleta.html', context)



def pedido(request):
    pass

@login_required
def ver_pedidos(request):
    cliente=Usuario.objects.get(id=request.session['id'])
    pedidos = Compra.objects.filter(cliente=cliente)
    if request.method == 'GET':
        context = {
            'pedidos': pedidos
        }
        return render(request, 'ver_pedidos.html', context)
    

