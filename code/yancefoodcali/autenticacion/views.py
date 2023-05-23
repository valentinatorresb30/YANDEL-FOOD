from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth,messages
from autenticacion.models import Usuario
from cliente.models import Categoria, Inventario


from cliente.views import InventarioController
# Create your views here.
class UsuarioController:

    def get_view_auth(request):
        return render(request,'auth.html')
    
    def autenticar(request):
        usuario = request.POST.get('usuario')
        password = request.POST.get('clave')
        try:
            user = User.objects.get(username=usuario,password=password)
            # print(user)
        except Exception as e:
            print(e.args)
            user = None
        if user is not None:
            auth.login(request,user)
            # return render(request,'clientes/menu.html',context={'inventario':inventario,'categorias':categorias})
            return redirect('menu')
        messages.error(request,"Credenciales incorrectas")
        return redirect('login')
    @login_required
    def logout_view(request):
        auth.logout(request)
        return redirect('login')
    
    def sing_up(request):
        nombre = request.POST.get('first-name')
        apellido = request.POST.get('last-name')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        usuario_form = request.POST.get('usuario')
        clave = request.POST.get('clave')

        try:
            credenciales = User.objects.create(password=clave,username=usuario_form,
                                               first_name=nombre,last_name=apellido,
                                               email=email)
            credenciales.save()
            usuario = Usuario(direccion=direccion,credenciales=credenciales)
            usuario.save()
            messages.success(request,"Registro Exitoso")
        except Exception as e:
            credenciales.delete()
            usuario.delete()
            print(e.args)
            messages.error(request,"No se pudo crear el usuario")
        return redirect('login')
        
        
        