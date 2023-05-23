# Generated by Django 4.1.7 on 2023-05-02 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=50, unique=True, verbose_name='nombre_categoria')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.categoria'),
        ),
    ]