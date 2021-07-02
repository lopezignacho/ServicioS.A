from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import connection
import cx_Oracle

# Create your views here.

@login_required
def home(request):
    agregar_usuario('lalos', 'palla', 'pollo', 'zz@hot.cl', 321)
    return render(request, 'app/home.html')


@login_required
def menu(request):
    return render(request, 'app/menu.html')

#@permission_required('auth.add_user')   Error de registro al tener comando (error en '_user' )
def agregar_usuario(username, nombre, apellido, correo, clave):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER) 
    cursor.callproc('SP_AGREGAR_USUARIO',[username, nombre, apellido, correo, clave, salida]) 
    return salida.getvalue()


# -------------------------------------------------- Agregar usuario ----------------------
def registro(request):
      mens={}
      #agregar_usuario
      if request.method == 'POST':
          username = request.POST.get('username')
          nombre = request.POST.get('nombre')
          apellido = request.POST.get('apellido')
          correo = request.POST.get('correo')
          clave = request.POST.get('clave')
          salida = agregar_usuario(username, nombre, apellido, correo, clave)
          
          if salida == 1:
              mens['mensaje'] ='se ha registrado el usuario'
          else:
              mens['mensaje']= 'no se ha podido guardar'
  
      return render(request, 'registration/registro.html')

#-------------------------------------------------------------------------------

#------------------------------- Modificar user ----------------------------------

def modificar_usuario(v_id,v_username, v_nombre, v_apellido, v_correo, v_clave):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_salida = cursor.var(cx_Oracle.NUMBER) 
    cursor.callproc('SP_MODIFICAR_USER ',[v_id, v_username, v_nombre, v_apellido, v_correo, v_clave, v_salida]) 
    return v_salida.getvalue()


def modificar(request):
      mens={}
      #modificar_usuario
      if request.method == 'POST':
          v_id= request.POST.get('id')
          v_username = request.POST.get('username')
          v_nombre = request.POST.get('nombre')
          v_apellido = request.POST.get('apellido')
          v_correo = request.POST.get('correo')
          v_clave = request.POST.get('clave')
          v_salida = modificar_usuario(v_id,v_username, v_nombre, v_apellido, v_correo, v_clave)
          
          if v_id == id : # Aqui ingresar valor de varible id a colocar en pagna modificar
           if v_salida == 1:
               mens['mensaje'] ='se ha modificar el usuario'
           else:
               mens['mensaje']= 'no se ha podido modificar'
          else:
              mens['mensaje']= 'no se ha podido modificar'
  
      return render(request, 'registration/modificar.html')

#---------------------------------------------------------------------------------------

# Eliminar user ------------------------------------------------------------------------
def eliminar_user(v_id, z_salida):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    z_salida = cursor.var(cx_Oracle.NUMBER) 
    cursor.callproc('SP_ELIMINAR_USER',[v_id]) 
    return z_salida.getvalue()
def iniciarsesion(request):
    return redirect (request,'registration/eliminar.html')


def modificar(request):
      mens={}
      #modificar_usuario
      if request.method == 'POST':
          v_id= request.POST.get('id')
          z_salida = modificar_usuario(v_id)
          
          if v_id == id : # Aqui ingresar valor de varible id a colocar en pagna modificar
           if z_salida == 1:
               mens['mensaje'] ='se ha eliminar el usuario'
           else:
               mens['mensaje']= 'no se ha podido eliminar'
          else:
              mens['mensaje']= 'no se ha podido eliminar'
  
      return render(request, 'registration/elimnar.html')





def listado_usuarios(request):
    data = {
        'listado_usuario':sp_listado_usuarios()
    }
    return render(request, 'app/listado_usuarios.html', data)

def sp_listado_usuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LIStADO_USUARIOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

@permission_required('auth.delete_user')
def eliminar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listado_usuarios")

def usuario(request):
    return render(request, 'app/usuario.html')