from .models import Page
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView # Clase modelo que se utiliza para recorrer modelos y mostrarlos en template
from django.views.generic.detail import DetailView # Clase modelo que se utiliza para mostrar el detalle en un template
from django.views.generic.edit import CreateView # Clase modelo que se utiliza para mostrar un template de creación
from django.views.generic.edit import UpdateView # Clase modelo que se utiliza para mostrar el template de actualización
from django.views.generic.edit import DeleteView # Clase modelo que se utiliza para mostrar el template de eliminación

# Dentro de los templates se puede acceder con "object" o con el "nombre del modelo"

# Create your views here.

# Al template hay que cambiarle el nombre y ponerle page_list
class PageListView(ListView):
    # Se especifica la lista de modelos
    model = Page
 
# Al template hay que cambiarle el nombre y ponerle page_detail   
class PageDetailView(DetailView):
    model = Page

class PageCreateView(CreateView):
    model = Page
    
    # Aqui especificamos los campos que queremos que se muestren para editar
    fields = ['title', 'content', 'order']
    
    # Método que permite redigir a una página cuando el formulario se envió de manera correcta
    #def get_success_url(self):
    #    return reverse('pages')
    
    # Método más facil que sobreescribir el método anterior
    success_url = reverse_lazy('pages')

class PageUpdateView(UpdateView):
    model = Page
    # Campos del modelo que se muestran para editar
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        # Se concatena un 'ok' para comprobar si la actualización se realizó correctamente
        return reverse_lazy('update_page', args=[self.object.id]) + '?ok'

class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')
