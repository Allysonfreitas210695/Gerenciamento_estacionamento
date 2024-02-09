# gerenciamento_estacionamento/serializers.py
from rest_framework import serializers
from .models import Cliente, Veiculo, Estacionamento, Tarifa

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'saldo', 'nome', 'endereco', 'telefone']

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['id', 'cliente', 'placa', 'modelo', 'cor', 'ano']

class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ['id', 'veiculo', 'hora_entrada', 'hora_saida', 'valor_pago', 'observacoes', 'status', 'tarifas']

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = ['id', 'descricao', 'valor_hora', 'valor_diaria', 'criado_em', 'atualizado_em']