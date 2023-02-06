from django.urls import path
from .views import ListaUsuariosListView

urlpatterns = [
    path("", ListaUsuariosListView.as_view(), name='lista_usuarios')
]