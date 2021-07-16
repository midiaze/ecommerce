from django.shortcuts import redirect, render
from apps.usuarios.formulario import UsuarioForm
from apps.usuarios.models import Usuario

# Create your views here.
def index(request):
    context = {
        'index': "Este es el index de usuarios"
    }
    return render(request, "index_usuarios.html", context)

def registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            nuevo = formulario.save()
            if nuevo.id == 1:
                nuevo.super_user = True
                nuevo.save()
            return redirect("usuarios:index")
    else:
        formulario = UsuarioForm()
    context = {
        'formulario_usuario' : formulario,
    }
    return render(request, "index_usuarios.html", context)

def login(request):
    if request.method == "GET":
        context = {
            'login': True
        }
        return render(request,"index_usuarios.html", context)
    if request.method == "POST":
        errors = Usuario.objects.validar_ingreso(request.POST)
        if len(errors)>0:
            context = {
                'login': True,
                'email': request.POST['email'],
                'errors': errors,
            }
            return render(request,"index_usuarios.html", context)
        else:
            usuario = Usuario.objects.get(email=request.POST['email'])
            request.session["id"]=usuario.id
            return redirect("productos:index")