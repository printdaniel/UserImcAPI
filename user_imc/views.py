from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializer import UsuariosSerializer
from .models import Usuarios
from django.db.models import Avg

class UsuariosCreateView(APIView):
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UsuariosRetrieveByNameView(RetrieveAPIView):
    serializer_class = UsuariosSerializer

    def get_object(self):
        nombre = self.kwargs['nombre']  # Obtén el nombre de la URL
        usuario = Usuarios.objects.get(username=nombre)
        return usuario

class UsuariosListView(ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class UsuariosRetrieveByIDView(RetrieveAPIView):
    serializer_class = UsuariosSerializer

    def get_object(self):
        id = self.kwargs['id']  # Obtén el id de la URL
        print(id)
        usuario = Usuarios.objects.get(id=id)
        return usuario

class EstadisticasView(APIView):
    def get(self, request):
        # Esatdísticas
        total_usuarios = Usuarios.objects.count()
        promedio_imc = Usuarios.objects.aggregate(promedio_imc=Avg('imc'))
        promedio_peso = Usuarios.objects.aggregate(promedio_peso=Avg('peso'))
        promedio_altura = Usuarios.objects.aggregate(promedio_altura=Avg('altura'))

        estadisticas = {
            'total_usuarios': total_usuarios,
            'promedio_imc': promedio_imc['promedio_imc'],
            'promedio_peso': promedio_peso['promedio_peso'],
            'promedio_altura': promedio_altura['promedio_altura'],
        }

        return Response(estadisticas)
