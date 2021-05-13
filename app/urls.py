from django.urls import path
from .views import home, contacto, menu, login, registro

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('menu', menu, name="menu"),
    path('login', login, name="login"),
    path('registro', registro, name="registro")
]

