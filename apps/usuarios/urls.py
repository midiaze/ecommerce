from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("", views.index, name="index"),
    path("registro", views.registro, name="registro"),
    path("login", views.login, name="login"),
]