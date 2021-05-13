from django import forms
from django.db.models import fields
from .models import Contacto 
from django import forms

 
class ContactoForm(forms.ModelForm): 

    class Meta: 
        model = Contacto       
        fields = '__all__' 