from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 


def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart={}
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
	return {'cartItems':cartItems, 'order':order, 'items':items}


def cartData(request):
	order = cookieCart(request)
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']
	return {'cartItems':cartItems,'order':order, 'items':items}