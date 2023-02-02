from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class EmailCreationForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingrese un email válido de no más de 250 caracteres')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']