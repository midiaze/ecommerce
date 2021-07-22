from django.db import models
from django.contrib.auth.models import User
from apps.productos.models import Producto


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    order_total = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.id)

    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total= self.product.price * self.quantity
        return total



class ShippingAddres(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address



# from django.db import models
# from apps.usuarios.models import Usuario
# from apps.productos.models import Producto
# Create your models here.
# class Compra(models.Model):
#     cliente = models.ForeignKey(Usuario, related_name="compras_cliente", on_delete=models.PROTECT)
#     total_compra = models.PositiveIntegerField()
#     ruta_boleta = models.CharField(max_length=255, default="")

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Pedido(models.Model):
#     compra = models.ForeignKey(Compra, related_name="pedido_detalle", on_delete=models.PROTECT)
#     producto = models.ForeignKey(Producto, related_name="pedidos", on_delete=models.PROTECT)
#     cantidad = models.PositiveSmallIntegerField()
#     precio_total = models.PositiveIntegerField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Carrito(models.Model):
#     producto = models.ForeignKey(Producto, related_name="carrito_producto", on_delete=models.CASCADE)
#     cliente = models.ForeignKey(Usuario, related_name="carrito_cliente", on_delete=models.CASCADE)
#     cantidad = models.PositiveSmallIntegerField()

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)




# class Product(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     price = models.DecimalField(max_digits=7, decimal_places=2)
#     digital = models.BooleanField(default=False, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.name

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
