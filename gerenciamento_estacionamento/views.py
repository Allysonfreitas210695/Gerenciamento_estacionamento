from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cliente, Veiculo, Estacionamento, Tarifa
from .serializers import ClienteSerializer, VeiculoSerializer, EstacionamentoSerializer, TarifaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        for data in serializer.data:
            veiculos = Veiculo.objects.filter(cliente=data['id'])
            veiculo_serializer = VeiculoSerializer(veiculos, many=True)
            data['veiculos'] = veiculo_serializer.data

        return Response(serializer.data)

class VeiculoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class EstacionamentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        for data in serializer.data:
            veiculos = Veiculo.objects.filter(id=data['veiculo'])
            veiculo_serializer = VeiculoSerializer(veiculos, many=True)
            data['veiculo'] = veiculo_serializer.data[0] if veiculo_serializer.data else None

            tarifas = Tarifa.objects.filter(id__in=data['tarifas'])
            tarifa_serializer = TarifaSerializer(tarifas, many=True)
            data['tarifas'] = tarifa_serializer.data

        return Response(serializer.data)


class TarifaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer