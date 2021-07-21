from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 


def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
		# print('Hola')
	except:
		cart={}
		print('Chao')
	# print('Cart:', cart)
	items = []
	order = {
		'get_cart_total':0, 
		'get_cart_items':0, 
		} 
	cartItems = order['get_cart_items']

	for i in cart:	
		try:
			cartItems += cart[i]['quantity']
			product = Producto.objects.get(id=i)
			total = (product.precio * cart[i]['quantity'])
			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']
			item = {
				'product':{
					'id':product.id,
					'nombre':product.nombre,
					'precio':product.precio,
					'descripcion':product.descripcion,
					'imagen':product.imagen,
					'stock':product.stock,
					'min_stock':product.min_stock,
					'categoria':product.categoria,
					},
				'quantity':cart[i]['quantity'],
				'get_total':total
				}
			items.append(item)
		except:
			pass
	print(cart)
	return {'cartItems':cartItems, 'order':order, 'items':items}


def cartData(request):
	# if 'id' in request.session:
	# customer = Customer.objects.get(id=request.session['id'])
	order = cookieCart(request)
		# items= order.orderitem_set.all()
		# cartItems = order.get_cart_items()
	# else:
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']
	
	return {'cartItems':cartItems,'order':order, 'items':items}
	

	
def guestOrder(request, data):
	print('user is not logged in ...')
	print ('COOKIES:', request.COOKIES)
	name=data['form']['name']
	email = data['form']['email']
	cookieData = cookieCart(request)
	items = cookieData['items']
	customer, created = Customer.objects.get_or_create(
		email=email,
	)
	
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer = customer,
		complete=False,
	)
	for item in items:
		product= Producto.objects.get(id=item['product']['id'])

		orderItem=OrderItem.objects.create(
			product=product,
			order=order,
			quantity=item['quantity']
		)
	return customer, order