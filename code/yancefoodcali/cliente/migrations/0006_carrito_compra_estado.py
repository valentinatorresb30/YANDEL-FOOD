# Generated by Django 4.1.7 on 2023-05-21 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_carrito_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito_compra',
            name='estado',
            field=models.BooleanField(blank=True, null=True, verbose_name='estado'),
        ),
    ]
