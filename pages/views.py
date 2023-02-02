from .models import Page
from django.urls import reverse_lazy
from django.views.generic.list import ListView # Clase modelo que se utiliza para recorrer modelos y mostrarlos en template
from django.views.generic.detail import DetailView # Clase modelo que se utiliza para mostrar el detalle en un template
from django.views.generic.edit import CreateView # Clase modelo que se utiliza para mostrar un template de creación
from django.views.generic.edit import UpdateView # Clase modelo que se utiliza para mostrar el template de actualización
from django.views.generic.edit import DeleteView # Clase modelo que se utiliza para mostrar el template de eliminación
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required # Importamos el decorador que verifica que el usuario sea miembro de l staff
from django.utils.decorators import method_decorator # Decorador que permite decorar métodos

# Diferencia entre reverse y reverse_lazy: https://es.stackoverflow.com/questions/258616/reverse-vs-reverse-lazy-django
# Dentro de los templates se puede acceder con "object" o con el "nombre del modelo"
# Un mixin es una implementación de una o varias funcionalidades para una clase

class StaffRequiredMixin(object):
    # Este mixin requerirá que el usuario sea miembro del staff
    
    # Sobreescribir este método es una alternativa para verificar que el miembro que intente ingresar a esta vista sea parte del staff
    def dispatch(self, request, *args, **kwargs):
        # Verificamos si el usuario forma parte del staff
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

    # Posterior a esto procedemos a heredar en las clases que se requieran
    # Se elimina el mixin debido a que hora usaremos un decorador


# Al template hay que cambiarle el nombre y ponerle page_list
class PageListView(ListView):
    # Se especifica la lista de modelos
    model = Page
 
# Al template hay que cambiarle el nombre y ponerle page_detail   
class PageDetailView(DetailView):
    model = Page

# --- Vistas para nuestro CRUD --- #

# --- Vista de creación
@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    
    # Vamos a pasarle el formulario que hemos creado
    form_class = PageForm
    
    # Aqui especificamos los campos que queremos que se muestren para editar
    # Se puede quitar esto debido a que nuestra clase de formulario ya lo incluye
    # fields = ['title', 'content', 'order']
    
    # Método que permite redigir a una página cuando el formulario se envió de manera correcta
    #def get_success_url(self):
    #    return reverse('pages')
    
    # Método más facil que sobreescribir el método anterior
    success_url = reverse_lazy('pages')

# --- Vista de actualización
@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    
    # Vamos a pasarle el formulario que hemos creado
    form_class = PageForm
    
    # Aqui especificamos los campos que queremos que se muestren para editar
    # Se puede quitar esto debido a que nuestra clase de formulario ya lo incluye
    # fields = ['title', 'content', 'order']
    
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        # Se concatena un 'ok' para comprobar si la actualización se realizó correctamente
        return reverse_lazy('update_page', args=[self.object.id]) + '?ok'

# --- Vista de eliminación
@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages')
