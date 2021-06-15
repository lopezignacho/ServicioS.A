from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm
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
    return render(request, 'app/home.html')

@login_required
def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "El mensaje ha sido enviado."
        else:
            data["form"] = formulario
            
    return render(request, 'app/contacto.html', data)

@login_required
def menu(request):
    return render(request, 'app/menu.html')

@permission_required('auth.add_user')
def agregar_usuario(username, nombre, apellido, correo, clave):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER) 
    cursor.callproc('SP_AGREGAR_USUARIO',[username, nombre, apellido, correo, clave, salida]) 
    return salida.getvalue()

def registro(request):

    #agregar_usuario
    if request.method == 'POST':
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')
        salida = agregar_usuario(username, nombre, apellido, correo, clave)
        if salida == 1:
            print ('se ha registrado el usuario')
        else:
            print ('no se ha podido guardar')

    return render(request, 'registration/registro.html')

def iniciarsesion(request):
    return redirect(request, 'registration/login.html')

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
