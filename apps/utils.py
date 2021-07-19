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
