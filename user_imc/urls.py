from django.urls import path
from .views import UsuariosCreateView, UsuariosRetrieveByNameView
urlpatterns = [
    path('usuarios/crear/', UsuariosCreateView.as_view(), name='usuarios-create'),
path('usuarios/<str:nombre>/', UsuariosRetrieveByNameView.as_view(), name='usuarios-retrieve-by-name'),
]
