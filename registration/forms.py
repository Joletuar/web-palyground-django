from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={
                'class':'form-control-file mt-3'
            }),
            'bio': forms.Textarea(attrs={
                'class':'form-control mt-3',
                'rows': 3,
                'placeholder': 'Ingrese su biografía'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Enlace'
            })
        }
class EmailProfileForm(forms.ModelForm):
    email = forms.EmailField(help_text='Ingrese un email válido de no más de 250 caracteres')
    class Meta:
        model = User
        fields = ['email']
    # Vamos a validar que el formulario sea único para cada usuario
    def clean_email(self):
        # Recuperamos el valor del campo email
        email = self.cleaned_data.get('email')
        
        # Verificamos primero si el campo email forma parte de la lista de campos que se han cambiado
        if 'email' in self.changed_data:
        # Verificamos si existe algun email ya en la base de datos
            if User.objects.filter(email=email).exists():
                # Si existe lanzamos un error
                raise forms.ValidationError("El email ya esta registrado, prueba con otro")
            return email