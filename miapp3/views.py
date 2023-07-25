# mi_app/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Producto, Pedido
from .forms import ClienteForm, ProductoForm, BusquedaForm

def cliente_view(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form})

def buscar_view(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados_clientes = Cliente.objects.filter(nombre__icontains=termino_busqueda)
            resultados_productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {'resultados_clientes': resultados_clientes, 'resultados_productos': resultados_productos})
    else:
        form = BusquedaForm()
    return render(request, 'buscar_form.html', {'form': form})

