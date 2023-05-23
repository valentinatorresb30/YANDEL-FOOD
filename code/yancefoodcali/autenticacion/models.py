from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    direccion = models.TextField(verbose_name="direccion",max_length=150,null=False,blank=False)
    credenciales = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="credenciales")
    class Meta:
        verbose_name_plural = "usuario"
        db_table = "usuario"
        verbose_name = "usuario"
