from apps.utils import login_dashboard, login_required
import re
from django.shortcuts import redirect, render
from apps.usuarios.formulario import UsuarioForm
from apps.usuarios.models import Usuario
import bcrypt

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
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            nuevo.password = hash1
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
            context = {
                'usuario': usuario,
            }
            return redirect("usuarios:dashboard",id_usuario=usuario.id)

def logout(request):
    request.session.clear()
    return redirect("usuarios:index")

@login_required
@login_dashboard
def dashboard(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    context = {
        'dashboard' : True,
        'usuario': usuario,
    }
    return render(request, "index_usuarios.html", context)

@login_required
@login_dashboard
def perfil(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "GET":
        context = {
            'perfil' : True,
            'usuario': usuario,
        }
        return render(request, "index_usuarios.html", context)
    if request.method == "POST":
        errors = Usuario.objects.validar_editar_usuario(request.POST)
        if usuario.email != request.POST['email']:
            errors['email'] = 'Email ya registrado, favor intentar con otro'
        if len(errors)>0:
            context = {
                'perfil' : True,
                'usuario': usuario,
                'errors': errors
            }
            return render(request, "index_usuarios.html", context)
        else:
            usuario.nombre = request.POST['nombre']
            usuario.direccion = request.POST['direccion']
            usuario.email = request.POST['email']
            usuario.save()
            return redirect("usuarios:dashboard",id_usuario=usuario.id)

@login_required
@login_dashboard
def cambiar_pw(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "GET":
        context = {
            'cambio_pw' : True,
            'usuario': usuario,
        }
        return render(request, "index_usuarios.html", context)
    if request.method == "POST":
        errors = Usuario.objects.validar_cambio_pw(request.POST)
        if not bcrypt.checkpw(request.POST['password'].encode(), usuario.password.encode()):
            errors['cambio_pw'] = 'Correo y contraseña no coinciden'
        if len(errors)>0:
            context = {
                'cambio_pw' : True,
                'usuario': usuario,
                'errors': errors
            }
            return render(request, "index_usuarios.html", context)
        else:
            hash2 = bcrypt.hashpw(request.POST['nueva_pw'].encode(), bcrypt.gensalt()).decode()
            usuario.password = hash2
            usuario.save()
            return redirect("usuarios:dashboard",id_usuario=usuario.id)

@login_required
@login_dashboard
def inactivar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.es_activo = 'False'
    usuario.save()    
    request.session.clear()
    return redirect("usuarios:index")