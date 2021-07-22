from django.db import models
from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from django.db.models import Sum


# class Customer(models.Model):
#     user = models.OneToOneField(Usuario, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name


class Order(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    order_total = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.id)

    @property
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
        total= self.product.precio * self.quantity
        return total



# class ShippingAddres(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=255, null=True)
#     city = models.CharField(max_length=255, null=True)
#     state = models.CharField(max_length=255, null=True)
#     zipcode = models.CharField(max_length=255, null=True)
#     date_added=models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.address
