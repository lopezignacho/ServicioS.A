from django import forms
from django.db.models import fields
from .models import Contacto 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

 
class ContactoForm(forms.ModelForm): 

    class Meta: 
        model = Contacto       
        fields = '__all__' 

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]