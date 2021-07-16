from apps.productos.models import Producto
from django.shortcuts import redirect, render
from apps.productos.formulario import CategoriaForm, ProductoForm

# Create your views here.
def index(request):
    context = {
        'index': "Este es el index de productos"
    }
    return render(request, "index_productos.html", context)

def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("productos:index")
    else:
        formulario = ProductoForm()
    context = {
        'formulario_producto' : formulario,
    }
    return render(request, "index_productos.html", context)
    
def crear_categoria(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("productos:index")
    else:
        formulario = CategoriaForm()
    context = {
        'formulario_categoria' : formulario,
    }
    return render(request, "index_productos.html", context)

def listado_productos(request):
    context = {
        'productos': Producto.objects.all()
    }
    return render(request, "index_productos.html", context)
        
        