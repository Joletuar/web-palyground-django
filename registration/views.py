
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import EmailCreationForm

# Create your views here.

class SignupView(CreateView):
    
    # Configuramos el formulario que debe de mostrar en la vista
    form_class = EmailCreationForm
    
    # Justo despues del registro redirigimos
    # success_url = reverse_lazy('login')
    
    # Especificamos el template que tiene que cargar
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    
    # Vamos a recuperar los campos del formulario que nos generó django
    def get_form(self, form_class=None):
        # Recuperamos el formulario que genera la clase
        form = super(SignupView, self).get_form()
        
        # Modificar en tiempo real los widgets del form
        form.fields['username'].widget = forms.TextInput(attrs={
            'class':'form-control mb-2',
            'label': '',
            'placeholder': 'Usuario'
        })
        form.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'label': '',
            'placeholder': 'Contraseña'
        })
        form.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control mb-2',
            'label': '',
            'placeholder': 'Repita su contraseña'
        })
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control mb-2',
            'label': '',
            'placeholder': 'Dirección de correo'
        })
        return form
