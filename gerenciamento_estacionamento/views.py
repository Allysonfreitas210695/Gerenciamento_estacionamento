import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication  # Importe SessionAuthentication aqui
from .models import Cliente, Veiculo, Estacionamento, Tarifa
from .serializers import ClienteSerializer, VeiculoSerializer, EstacionamentoSerializer, TarifaSerializer

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ClienteViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]    
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class EstacionamentoViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]   
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class TarifaViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]   
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer