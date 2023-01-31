from django.urls import path
from . import views

# Para llamar las vistas CBV se utiliza su método interno .as_view()

urlpatterns = [
    path('', views.HomePaView.as_view(), name="home"),
    path('sample/', views.SamplePaView.as_view(), name="sample"),
]