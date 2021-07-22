from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
	path('update_item', views.updateItem, name="update_item"),
    path('process_order', views.processOrder, name="process_order"),
    path('previous_orders', views.previous_orders, name="previous_orders"),
    path('order_details/<int:order_id>', views.order_details, name="order_details"),
    path('none', views.none, name="none"),
    path('eliminar', views.eliminar, name="eliminar"),
    # path('add/<int:productId>/<int:quantity>', views.update_order, name="add_product"),

]