from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Carrito_compra,Usuario,Venta,Detalle_venta
from django.contrib import messages


from cliente.models import Categoria, Inventario

# Create your views here.

class InventarioController:
    @login_required(login_url='login')
    def getAllInventario(request):
        inventario = Inventario.objects.select_related('producto_id').filter(cantidad__gt=0)
        carrito={}
        total = 0
        # print(inventario)
        categorias = Categoria.objects.all()
        if request.user.is_authenticated:
            usuario = Usuario.objects.get(credenciales=request.user.id)
            carrito = Carrito_compra.objects.filter(fk_usuario=usuario.id,estado=True)
            for x in carrito:
                total += x.valor
        return render(request,'clientes/menu.html',context={'inventario':inventario,
                                                            'categorias':categorias,
                                                            'carrito':carrito,
                                                            'total_carrito':total})
    
    @login_required
    def detalle_producto(request,id_prod):
        producto = Inventario.objects.select_related('producto_id').get(producto_id=id_prod)
        return render(request,'clientes/detalle_producto.html',{'detalle':producto})

class CarritoController:
    # @login_required(login_url='login')
    # def add_carrito(request):
    #     inv_id = request.POST.get('inv_id')
    #     user_id = request.POST.get('user_id')
    #     cantidad = request.POST.get('cantidad')
    #     try:
    #         inv = Inventario.objects.get(pk=inv_id)
    #         usuario = Usuario.objects.select_related('credenciales').get(credenciales=user_id)
    #         carrito = Carrito_compra(fk_producto=inv.producto_id,cantidad=cantidad,
    #                                 fk_usuario=usuario,valor=int(cantidad)*int(inv.producto_id.precio_unitario))
    #         carrito.save()
    #     except Exception as e:
    #         print(e.args)
    #     return redirect('menu')

    @login_required(login_url='login')
    def add_carrito(request):
        inv_id = request.POST.get('id_inv')
        user_id = request.user.id
        cantidad = request.POST.get('cant')
        inv = Inventario.objects.get(pk=inv_id)
        usuario = Usuario.objects.select_related('credenciales').get(credenciales=user_id)
        existe = None
        try:
            existe = Carrito_compra.objects.get(fk_producto=inv.producto_id,fk_usuario=usuario.pk,estado=True)
        except Exception as ex:
            existe = None
            print(ex.args)
        try:
            if existe is not None:
                old_cant=existe.cantidad
                existe.cantidad = int(old_cant) + int(cantidad)
                existe.valor = int(existe.fk_producto.precio_unitario)* existe.cantidad
                existe.save()
                messages.success(request,'Producto modificado')
            else:
                carrito = Carrito_compra(fk_producto=inv.producto_id,cantidad=cantidad,
                                        fk_usuario=usuario,valor=int(cantidad)*int(inv.producto_id.precio_unitario))
                carrito.save()
                messages.success(request,'Producto agregado')
        except Exception as e:
            print(e.args)
            messages.error(request,'No se pudo agregar el prodcuto')
        return redirect('menu')
    
    @login_required(login_url='login')
    def delete_item(request,id_car):
        try:
            item = Carrito_compra.objects.get(pk=id_car)
            item.estado=False
            item.save()
            messages.success(request,'Item eliminado correctamente!')
        except Exception as e:
            print(e.args)
            messages.error(request,'No se pudo eliminar el item')
        return redirect('menu')


class VentaController:
    @login_required(login_url='login')
    def finalizarCompra(request):
        user_id = request.user.id
        total = 0
        cantidad = 0
        descripciones = []
        try:
            usuario = Usuario.objects.get(credenciales = user_id)
            carrito = Carrito_compra.objects.filter(fk_usuario=usuario.pk,estado = True)
            for x in carrito:
                total += x.valor
                cantidad += x.cantidad
            venta = Venta(total=total,fk_usuario=usuario)
            venta.save()
            for y in carrito:
                detalle = Detalle_venta(fk_producto=y.fk_producto,cantidad_comprada=y.cantidad,fk_venta=venta,valor=y.valor)
                inv = Inventario.objects.get(producto_id=y.fk_producto)
                detalle.save()
                y.estado=False
                inv.cantidad -= y.cantidad
                inv.save()
                y.save()
            descripciones = Detalle_venta.objects.filter(fk_venta = venta)
            
            messages.success(request,'Venta exitosa!')
        except Exception as e:
            print(e.args)
            messages.error(request,'Venta fallida!')
        
        return render(request,'clientes/factura.html',{'detalles':descripciones,'total':total,
                                                       'cantidad':cantidad})

    