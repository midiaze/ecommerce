from django.http.response import HttpResponse
from apps.utils import login_dashboard, login_required
import re
from django.shortcuts import redirect, render
from apps.usuarios.formulario import UsuarioForm
from apps.usuarios.models import Usuario
import bcrypt

# Create your views here.
def index(request): ##esta no se va a usar más, después hay que poner pass
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
            request.session["id"]=nuevo.id
            if nuevo.id == 1:
                return redirect("reportes:index")
            return redirect("usuarios:dashboard",id_usuario=nuevo.id) #esta redirecciona cuando entra después de registrarse un cliente
    else:
        formulario = UsuarioForm()
    context = {
        'formulario_usuario' : formulario,
    }
    return render(request, "usuarios/registro.html", context)

def login(request):
    if request.method == "GET":
        context = {
            'login': True
        }
        return render(request,"usuarios/login.html", context)
    if request.method == "POST":
        errors = Usuario.objects.validar_ingreso(request.POST)
        if len(errors)>0:
            context = {
                'login': True,
                'email': request.POST['email'],
                'errors': errors,
            }
            return render(request,"usuarios/login.html", context)
        else:
            usuario = Usuario.objects.get(email=request.POST['email'])
            request.session["id"]=usuario.id
            if not usuario.super_user:
                context = {
                    'usuario': usuario,
                }
                return redirect("usuarios:dashboard",id_usuario=usuario.id) #esta redirecciona cuando entra después de login un cliente
            if usuario.super_user:
                return redirect("reportes:index")

def logout(request):
    request.session.clear()
    return redirect("/")

@login_required
def dashboard(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    context = {
        'dashboard' : True,
        'usuario': usuario,
    }
    return render(request, "index.html", context) #o cambiar solo esta a redirecto de carrito con productos

@login_required
def perfil(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "GET":
        context = {
            'perfil' : True,
            'usuario': usuario,
        }
        if not usuario.super_user:
            return render(request, "usuarios/perfil_clientes.html", context)
        else:
            print("si estamos aki")
            return render(request, "restaurante/perfil_restaurante.html", context)
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
            if not usuario.super_user:
                return render(request, "usuarios/perfil_clientes.html", context)
            else:
                return render(request, "restaurante/perfil_restaurante.html", context)
        else:
            usuario.nombre = request.POST['nombre']
            usuario.direccion = request.POST['direccion']
            usuario.email = request.POST['email']
            usuario.save()
            if not usuario.super_user:
                return redirect("usuarios:dashboard",id_usuario=usuario.id)
            else:
                return redirect("usuarios:restaurante")

@login_required
def cambiar_pw(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    if request.method == "GET":
        context = {
            'cambio_pw' : True,
            'usuario': usuario,
        }
        if not usuario.super_user:
            return render(request, "usuarios/perfil_clientes.html", context)
        else:
            return render(request, "restaurante/perfil_restaurante.html", context)
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
            if not usuario.super_user:
                return render(request, "usuarios/perfil_clientes.html", context)
            else:
                return render(request, "restaurante/perfil_restaurante.html", context)
        else:
            hash2 = bcrypt.hashpw(request.POST['nueva_pw'].encode(), bcrypt.gensalt()).decode()
            usuario.password = hash2
            usuario.save()
            if not usuario.super_user:
                return redirect("usuarios:dashboard",id_usuario=usuario.id)
            else:
                return redirect("usuarios:restaurante")

@login_required
def inactivar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id=id_usuario)
    usuario.es_activo = 'False'
    usuario.save()    
    request.session.clear()
    return redirect("/")

def restaurante(request):
    usuario = Usuario.objects.get(id=request.session['id'])
    context = {
        'usuario': usuario
    }
    return redirect("reportes:index",id_usuario=usuario.id)