from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_producto", views.crear_producto, name="crear_producto"),
    path("crear_categoria", views.crear_categoria, name="crear_categoria"),
    path("listado_productos", views.listado_productos, name="listado_productos"),
]