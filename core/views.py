from django.shortcuts import render
from django.views.generic.base import TemplateView # Esta clase es la que mejor se adapta para renderizar un template

# Vamos a adaptar estas vistas basadas en funciones a vistas basadas en clases
# Para hacer esto tenemos que buscar en la documentación de django que clase se adapta mejor a lo que queremos hacer
# Estas vistas se llaman de manera diferente dentro de las urls

#def home(request):
#    return render(request, "core/home.html")

#def sample(request):
#    return render(request, "core/sample.html")


# Redifinición dela vista home

class HomePaView(TemplateView):
    
    # En este atributo especificamos la ruta del template a renderizar
    template_name = "core/home.html"
    
    # Este método permite extender el diccionario de contexto que tiene la vista
    # Es similar a pasar los parámetros por diccionario
    
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Mi página web"
        return context""" 

    # Existe otra forma mucho mas fácil de extener el dict de contexto del template
    # Se puede usar la forma convencional de retornar render
    # Para hacer esto se debe de sobreescribir el método get
    
    def get(self, request, *args, **kargs):
        return render(request, self.template_name, {'title': "Mi página web"})

# Redifinición dela vista sample

class SamplePaView(TemplateView):
    # En este atributo especificamos la ruta del template a renderizar
    template_name = "core/sample.html"