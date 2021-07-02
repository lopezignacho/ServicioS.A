from django.urls import path
from .views import home, menu, login, registro, listado_usuarios, eliminar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('menu', menu, name="menu"),
    path('login', login, name="login"),
    path('registro/', registro, name="registro"),
    path('listado-usuarios', listado_usuarios, name="listado_usuarios"),
    path('eliminar-usuario/<id>/', eliminar_usuario, name="eliminar_usuario"),
]

