from django.urls import path
from django.views.generic import TemplateView
from .views import UsuarioController

urlpatterns=[
    path('',UsuarioController.get_view_auth,name='login'),
    path('autenticar',UsuarioController.autenticar,name='autenticar'),
    path('logout',UsuarioController.logout_view,name='logout'),
    path('sign-up',UsuarioController.sing_up,name='sign-up'),
]