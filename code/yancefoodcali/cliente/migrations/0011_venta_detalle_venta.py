# Generated by Django 4.1.7 on 2023-05-23 21:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0002_rename_direccioon_usuario_direccion'),
        ('cliente', '0010_alter_carrito_compra_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='total')),
                ('fecha', models.DateField(default=datetime.datetime(2023, 5, 23, 16, 3, 18, 671717), verbose_name='fecha')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_comprada', models.IntegerField(verbose_name='cantidad_comprada')),
                ('valor', models.IntegerField(verbose_name='valor')),
                ('fk_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.producto')),
                ('fk_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.usuario')),
            ],
        ),
    ]
