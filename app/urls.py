from django.urls import path
from .views import home, contacto, menu, login

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('menu', menu, name="menu"),
    path('login', login, name="login"),
]

