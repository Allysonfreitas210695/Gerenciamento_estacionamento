# gerenciamento_estacionamento/serializers.py
from rest_framework import serializers
from .models import Cliente, Veiculo, Estacionamento, Tarifa

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = "__all__"

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = "__all__"