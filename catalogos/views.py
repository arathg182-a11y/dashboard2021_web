from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Categoria, Cliente, Producto, Sucursal, Vendedor, MetodoPago

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'catalogos/lista_categorias.html', {'categorias': categorias})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'catalogos/lista_clientes.html', {'clientes': clientes})

@login_required
def lista_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'catalogos/lista_productos.html', {'productos': productos})

@login_required
def lista_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'catalogos/lista_sucursales.html', {'sucursales': sucursales})

@login_required
def lista_vendedores(request):
    vendedores = Vendedor.objects.select_related('sucursal').all()
    return render(request, 'catalogos/lista_vendedores.html', {'vendedores': vendedores})

@login_required
def lista_metodos_pago(request):
    metodos = MetodoPago.objects.all()
    return render(request, 'catalogos/lista_metodos_pago.html', {'metodos': metodos})
