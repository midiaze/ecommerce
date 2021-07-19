from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_producto", views.crear_producto, name="crear_producto"),
    path("carga_masiva", views.carga_masiva, name="carga_masiva"),
    path("crear_categoria", views.crear_categoria, name="crear_categoria"),
    path("listado_productos", views.listado_productos, name="listado_productos"),
    path("editar_producto/<int:id_producto>", views.editar_producto, name="editar_producto"),
    path("/eliminar_producto/<int:id_producto>", views.eliminar_producto, name="eliminar_producto"),

]