from django.urls import path
from .views import UsuariosCreateView, UsuariosRetrieveByNameView, UsuariosListView

urlpatterns = [
    path('registrar-usuario/', UsuariosCreateView.as_view(), name='registrar'),
    path('usuarios/<str:nombre>/', UsuariosRetrieveByNameView.as_view(), 
         name='usuarios-retrieve-by-name'),
    path('usuarios', UsuariosListView.as_view(), name='lista-registros'),
]
