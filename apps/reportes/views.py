from django.db.models import query
from django.shortcuts import render
from django.db.models import Avg, Sum, Count
from .models import *
import datetime
from apps.pedidos.models import OrderItem, Order
from apps.productos.models import Producto
from apps.usuarios.models import Usuario

def index(request):
    usuario = Usuario.objects.get(id = request.session['id'])
    #este año
    year = datetime.datetime.now().year
    first_week = datetime.datetime(year,1,1)
    last_week = first_week + datetime.timedelta(365)
    print(f'first_week:{first_week}')
    print(f'last_week:{last_week}')

    #esta semana
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)

    #demanda
    year_ago = year - 1
    month = datetime.datetime.now().month
    day = start_week.day #datetime.datetime.now().day
    date_ago_start = datetime.datetime(year_ago,month,day)
    date_ago_end = date_ago_start + datetime.timedelta(7)

    sales = Order.objects.filter(date_ordered__year=2021).values('date_ordered__month').distinct().annotate(total_sales = Sum('order_total'))

    context = {
        'usuario' : usuario,
        #esta semana
        'ventas_semanales_agregadas' : Order.objects.filter(date_ordered__range=[start_week, end_week]).aggregate(Sum('order_total')),
        'ventas_semanales': Order.objects.filter(date_ordered__range=[start_week, end_week]).values('date_ordered').annotate(sales = Sum('order_total')),
        'pedidos_semanales' : Order.objects.filter(date_ordered__range=[start_week, end_week]).values('date_ordered').annotate(total_orders = Count('id')),
        
        #este año
        'ventas_anuales_agregadas' : Order.objects.filter(date_ordered__range=[first_week, last_week]).aggregate(Sum('order_total')),
        'ventas' : Order.objects.filter(date_ordered__year=2021).values('date_ordered__month').distinct().annotate(total_sales = Sum('order_total')),
        'productos_vendidos' : OrderItem.objects.filter(date_ordered__range=[first_week, last_week]).values('product_id').annotate(total_quantity = Sum('quantity')),
        'pedidos_anuales'  : Order.objects.filter(date_ordered__range=[first_week, last_week]).values('date_ordered__month').annotate(total_orders = Count('id')),
        
        
        #demanda
        'demanda_hoy': Order.objects.filter(date_ordered__range=[first_week, last_week]).values('date_ordered').annotate(sum=Sum('order_total')),
        'demanda_pasada': Order.objects.filter(date_ordered__range=[date_ago_start, date_ago_end]).values('date_ordered').annotate(sum=Sum('order_total')),
        'customers' :Order.objects.filter(date_ordered__year=2021).values('customer_id').annotate(order_total = Count('customer_id')),

        #stock
        'stock' : Producto.objects.all().order_by('stock'),
        
    }
    return render(request, "reportes/chart.html", context)
