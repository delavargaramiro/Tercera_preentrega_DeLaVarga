from django.urls import path, include
from .views import *

urlpatterns = [
    path('cliente/', cliente_view, name="clientes"),
    path('producto/', producto_view, name="producto"),
    path('buscar/', buscar_view, name="buscar"),
    


    
]