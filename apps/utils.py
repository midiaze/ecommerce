from django.shortcuts import redirect
from apps.usuarios.models import Usuario
from django.core.exceptions import PermissionDenied


def login_required(view):
    
    def view_envuelta(request, *args, **kwargs):
        if 'id' in request.session:
            return view(request, *args, **kwargs)
        else:
            return redirect('/auth')

    return view_envuelta

def login_dashboard(view):
    def view_envuelta(request, id_usuario):
        usuario = Usuario.objects.get(id=id_usuario)
        if usuario.id != request.session['id'] or usuario.es_activo == "False":
            raise PermissionDenied()
        else:
            return view(request, id_usuario)
<<<<<<< HEAD
    
    return view_envuelta
=======

    return view_envuelta
>>>>>>> f90a1cd (push ignacia)
