from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.models import User

# Create your views here.

class ListaUsuariosListView(ListView):
    model = User