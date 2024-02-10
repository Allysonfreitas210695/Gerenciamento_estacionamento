from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Veiculo, Estacionamento, Tarifa
from .serializers import ClienteSerializer, VeiculoSerializer, EstacionamentoSerializer, TarifaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class EstacionamentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class TarifaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer