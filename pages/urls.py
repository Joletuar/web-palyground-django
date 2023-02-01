from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'), # El modelo espera el id con el nombre pk
    path('create/', views.PageCreateView.as_view(), name='create_page')
]

# Existe otra forma que declarar las urls
"""
pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='page'),
    path('create/', views.PageCreateView.as_view(), name='page_create')
], 'pages')
"""

# Al realizar esto debemos de tambien cambiar el modo en que se importan las urls dentro del archivo urls.py del proyecto principal.
# Con esto realizado ahora al momento de referencia un url dentro de los templates se debe realizarlo de la siguiente forma:
# pages:pages, pages:page, pages:create