# mi_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, BusquedaForm, PedidoForm


def index(request):
    return render(request, "miapp3/base.html")

def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'miapp3/cliente_form.html', {'form': form})

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'miapp3/producto_form.html', {'form': form})

def buscar_view(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados_clientes = Cliente.objects.filter(nombre__icontains=termino_busqueda)
            resultados_productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            resultados_pedidos = Pedido.objects.filter(cliente__nombre__icontains=termino_busqueda) | Pedido.objects.filter(producto__nombre__icontains=termino_busqueda)
            return render(request, 'miapp3/resultados_busqueda.html', 
                          {'resultados_clientes': resultados_clientes, 'resultados_productos': resultados_productos, 'resultados_pedidos': resultados_pedidos,})
    else:
        form = BusquedaForm()
    return render(request, 'miapp3/buscar_form.html', {'form': form})

def pedido_view(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)  
            pedido.total = pedido.cantidad * pedido.producto.precio
            pedido.save()  
            return redirect('pedido') 
    else:
        form = PedidoForm()
    return render(request, 'miapp3/pedido_form.html', {'form': form})
