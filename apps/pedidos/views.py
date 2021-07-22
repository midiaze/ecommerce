from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
#from weasyprint import HTML
from apps.utils import login_required


def store(request):
    products = Producto.objects.all()
    if 'id' in request.session:
        data = cartData(request)
        usuario =Usuario.objects.get(id=request.session['id'])
        cartItems = data['cartItems']
        context = {
            'products': products,
            'cartItems':cartItems,
        }
        return render(request, 'store/store.html', context)
    else:
        context = {
            'products':products
        }
        return render(request, 'store/store.html', context)
        

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems
    }
    return render(request, 'store/cart.html', context)


@csrf_exempt
def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items':items,
        'order':order,
        'cartItems': cartItems
    }
    return render(request, 'store/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	# print('Action:', action)
	# print('Product:', productId)

	usuario = Usuario.objects.get(id=request.session['id'])
	product = Producto.objects.get(id=productId)
	order, created = Order.objects.get_or_create(usuario=usuario, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def processOrder(request):
    if request.method == 'POST':

        transaction_id = datetime.datetime.now().timestamp()
        # data = json.loads(request.body)

        if 'id' in request.session:
            usuario = Usuario.objects.get(id=request.session['id'])
            data = cartData(request)
            cartItems = data['cartItems']
            order1 = data['order']
            items = data['items']
            print('-'*60)
            print(cartItems)
            print(order1['get_cart_total'])
            print(items)
            print('-'*60)
            order = Order.objects.create(usuario=usuario, complete = True, order_total=order1['get_cart_total'])
            for item in items:
                product = Producto.objects.get(id=item['product']['id'])
                OrderItem.objects.create(product=product, order=order, quantity=item['quantity'])
            # total = (data['form']['total'])
            # order.transaction_id = transaction_id
            # if total == (order.get_cart_total()):
            #     order.complete = True
            # else: 
            #     return JsonResponse('error', safe=False)
            # order.save()
            request.session['complete']='Eliminar'

            # return JsonResponse('Payment complete', safe=False)       
    return redirect ('pedidos:store')

def eliminar(request):
    if request.method == 'GET':
        request.session['complete'] = ''
    return redirect('pedidos:store')


def previous_orders(request):
    data = cartData(request)
    cartItems = data['cartItems']
    if 'id' in request.session:
        usuario = Usuario.objects.get(id=request.session['id'])
        print(usuario.id)
        orders = Order.objects.filter(usuario=usuario)
        # if len(orders) == 0:
        #     return redirect('/pedidosnone')
        # else:
        context = {
            'orders':orders,
            'cartItems':cartItems
        }
        return render(request, 'store/previous_orders.html', context)

def none(request):
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems' : cartItems,
    }
    return render(request, 'store/none.html', context)

def order_details(request, order_id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = Order.objects.get(id=order_id)
    orderItems= OrderItem.objects.filter(order=order)
    context = {
        'order':order,
        'items':orderItems,
    }
    return render(request, 'store/order_details.html', context)



# def boleta(request, pedido_id):
#     pedido = Pedido.objects.get(id=pedido_id)
#     context={            
#         'pedido': pedido
#         }
#     Path('static/pdf').mkdir(parents=True, exist_ok=True)
#     nombreArchivo = f'boleta_{pedido.id}'
#     template = get_template(f'boleta_{pedido.id}.html')
#     html_template = template.render(context)
#     pdf_url = os.path.join(settings.BASE_DIR, 'static/pdf/'+nombreArchivo)
#     HTML(string = html_template).write_pdf(target=f'{pdf_url}.pdf')
#     return render(request, 'paginas/boleta.html', context)



