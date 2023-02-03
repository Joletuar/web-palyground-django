from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class EmailCreationForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingrese un email válido de no más de 250 caracteres')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # Vamos a validar que el formulario sea único para cada usuario
    def clean_email(self):
        # Recuperamos el valor del campo email
        email = self.cleaned_data.get('email')
        # Verificamos si existe algun email ya en la base de datos
        if User.objects.filter(email=email).exists():
            # Si existe lanzamos un error
            raise forms.ValidationError("El email ya esta registrado, prueba con otro")
        return email