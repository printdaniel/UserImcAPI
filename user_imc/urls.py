from django.urls import path
from .views import UsuariosCreateView, UsuariosRetrieveByNameView,UsuariosListView, UsuariosRetrieveByIDView, EstadisticasView

urlpatterns = [
    path('api/registrar-usuario/', UsuariosCreateView.as_view(), name='registrar'),
    path('api/usuarios/<str:nombre>/', UsuariosRetrieveByNameView.as_view(), 
         name='usuarios-retrieve-by-name'),
    path('api/usuarios', UsuariosListView.as_view(), name='lista-registros'),
    path('api/usuarios/<int:id>/', UsuariosRetrieveByIDView.as_view(), name='usuario-id'),
    path('api/estadisticas/', EstadisticasView.as_view(), name='estadisticas'),
]
