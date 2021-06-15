from django.urls import path
from .views import home, contacto, menu, login, registro, listado_usuarios, eliminar_usuario

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('menu/', menu, name="menu"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('listado-usuarios/', listado_usuarios, name="listado_usuarios"),
    path('eliminar-usuario/<username>/', eliminar_usuario, name="eliminar_usuario"),
    #path('modificar-usuario/<username>/', modificar_usuario, name="modificar_usuario"),
]

