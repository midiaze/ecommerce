from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.index, name="index"),
    path("boleta", views.boleta, name="boleta"),
    path("pedidos", views.ver_pedidos, name="ver_pedidos"),
]