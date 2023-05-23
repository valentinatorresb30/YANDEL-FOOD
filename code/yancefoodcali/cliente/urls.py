from django.urls import path
from django.views.generic import TemplateView
from .views import InventarioController,CarritoController,VentaController

urlpatterns=[
    path('menu',InventarioController.getAllInventario,name='menu'),
    path('add_carrito',CarritoController.add_carrito,name='add_carrito'),
    path('detalle/<int:id_prod>/',InventarioController.detalle_producto,name='detalle'),
    path('eliminar/<int:id_car>',CarritoController.delete_item,name='eliminar'),
    path('finalizar',VentaController.finalizarCompra,name='finalizar'),
]