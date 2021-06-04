from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required

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
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Te has registrado correctamente.")
            return redirect(to="home")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)

def iniciarsesion(request):
    return redirect(request, 'registration/login.html')
