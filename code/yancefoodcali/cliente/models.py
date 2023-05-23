from datetime import datetime
from django.db import models

from autenticacion.models import Usuario

# Create your models here.
class Categoria(models.Model):
    nombre_categoria= models.CharField(verbose_name="nombre_categoria",null=False,blank=False
                                       ,max_length=50,unique=True)
    class meta:
        verbose_name_plural = "categoria"
        db_table = "categoria"
        verbose_name = "categoria"

class Producto(models.Model):
    nombre= models.CharField(verbose_name="nombre",null=False,blank=False,max_length=50)
    descripcion= models.CharField(verbose_name="descripcion",null=False,blank=False,max_length=100)
    precio_unitario= models.IntegerField(verbose_name="precio_unitario",null=False,blank=False)
    detalle_producto= models.CharField(verbose_name="detalle_producto",null=False,blank=False,max_length=200)
    imagen = models.ImageField(upload_to='opciones_menu',null=True)
    categoria_id= models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    class meta:
        verbose_name_plural = "producto"
        db_table = "producto"
        verbose_name = "producto"

class Inventario(models.Model):
    producto_id = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad= models.IntegerField(verbose_name="cantidad",null=False,blank=False)
    class meta:
        verbose_name_plural = "inventario"
        db_table = "inventario"
        verbose_name = "inventario"

class Carrito_compra(models.Model):
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField(verbose_name="cantidad",blank=False,null=False)
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    valor = models.IntegerField(verbose_name='valor',null=False,blank=False)
    estado = models.BooleanField(verbose_name='estado',editable=True,null=False,default=True)
    class meta:
        verbose_name_plural = "carrito_compra"
        db_table = "carrito_compra"
        verbose_name = "carrito_compra"

class Venta(models.Model):
    total = models.IntegerField(verbose_name="total",blank=False,null=False)
    fk_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name='fecha',null=False,blank=False,default=datetime.now())
    estado = models.BooleanField(verbose_name='estado',editable=True,null=False,default=True)
    class meta:
        verbose_name_plural = "venta"
        db_table = "venta"
        verbose_name = "venta"

class Detalle_venta(models.Model):
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad_comprada = models.IntegerField(verbose_name="cantidad_comprada",blank=False,null=False)
    fk_venta = models.ForeignKey(Venta,on_delete=models.CASCADE)
    valor = models.IntegerField(verbose_name='valor',null=False,blank=False)
    class meta:
        verbose_name_plural = "detalle_venta"
        db_table = "detalle_venta"
        verbose_name = "detalle_venta"