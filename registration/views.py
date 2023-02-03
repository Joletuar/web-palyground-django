
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .forms import EmailCreationForm, ProfileForm, EmailProfileForm
from .models import Profile

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

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    form_class = ProfileForm
    
    def get_object(self):
        # Recuperar el objeto que se va a editar
        
        # Usamos un método para recuperar un objeto o crearlo al momento
        profile,created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'
    form_class = EmailProfileForm
    
    def get_object(self):
        # Recuperar el objeto que se va a editar
        return self.request.user

    def get_form(self, form_class=None):
        # Recuperamos el formulario que genera la clase
        form = super(EmailUpdate, self).get_form()
        
        # Modificar en tiempo real los widgets del form
        form.fields['email'].widget = forms.EmailInput(attrs={
            'class':'form-control mb-2',
            'placeholder': 'Email'
        })
        return form