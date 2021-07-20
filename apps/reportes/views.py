from django.db.models import query
from django.shortcuts import render
from django.db.models import Avg, Sum, Count
from .models import *
import datetime
from apps.productos.models import Producto
from apps.pedidos.models import Order, OrderItem

def index(request):
    #este año
    year = datetime.datetime.now().year
    first_week = datetime.datetime(year,1,1)
    last_week = first_week + datetime.timedelta(365)
    #esta semana
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)

    #demanda
    year_ago = year - 1
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    date_ago_start = datetime.datetime(year_ago,month,day)
    date_ago_end = date_ago_start + datetime.timedelta(7)
    print(date_ago_start)
    print(date_ago_end)

    context = {
        #este mes
        'ventas_semanales_agregadas' : Compra.objects.filter(created_at__range=[start_week, end_week]).aggregate(Sum('total_compra')),
        'ventas_anuales_agregadas' : Compra.objects.filter(created_at__range=[first_week, last_week]).aggregate(Sum('total_compra')),
        'ventas_semanales': Compra.objects.filter(created_at__range=[start_week, end_week]),
        
        #este año
        'ventas' : Compra.objects.filter(created_at__year=2021).order_by('created_at'),
        'productos_vendidos' : Pedido.objects.filter(created_at__range=[first_week, last_week]).values('producto_id').annotate(Sum('cantidad')),
        'pedidos'  : Pedido.objects.annotate(Count('id')),
        
        #demanda
        'demanda_hoy': Compra.objects.filter(created_at__range=[first_week, last_week]),
        'demanda_pasada': Compra.objects.filter(created_at__range=[date_ago_start, date_ago_end]),
        'stock' : Producto.objects.all().order_by('stock'),
        'frecuencia' : Compra.objects.all(),
        'data': Compra.objects.all()    
    }
    return render(request, 'chart.html', context)