from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("", views.index, name="index"),
    path("registro", views.registro, name="registro"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("dashboard/<int:id_usuario>", views.dashboard, name="dashboard"),
    path("perfil/<int:id_usuario>", views.perfil, name="perfil"),
    path("cambiar_pw/<int:id_usuario>", views.cambiar_pw, name="cambiar_pw"),
    path("/inactivar_usuario/<int:id_usuario>", views.inactivar_usuario, name="inactivar_usuario"),
    path("restaurante", views.restaurante, name="restaurante"),
]