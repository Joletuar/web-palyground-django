from django import forms
from .models import *

 # Se puede enlazar un modelo a un form para que se genere automaticamente
 
class PageForm(forms.ModelForm):
     
    # Dentro de esta clase enlazamos el modelo del cual queremos que se genere el formulario
    class Meta:
        model = Page 
        
        # Especificamos los campos que serán editables
        fields = ['title', 'content', 'order']
        
        # Especificamos los widgets para campo junto con respectivos atributos
        # Dentro le pasamos un diccionario con el nombre de las etiquetas del html a la que le quermos añaidr o cambiar atributos entre otros parámetros
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Ingrese un titulo"
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Ingrese una descripción"
            }),
            'order': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Elija un orden"
            })
        }
        
        # Podemos especificar lo que se muestra en los labels
        labels = {
            'title': '', 'oder':'', 'content':''
        }
