# gerenciamento_estacionamento/serializers.py
from rest_framework import serializers
from .models import Cliente, Veiculo, Estacionamento, Tarifa

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().update(instance, validated_data)
    
class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().update(instance, validated_data)

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().update(instance, validated_data) 
    
class EstacionamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estacionamento
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user and user.is_authenticated:
            validated_data['user'] = user
        return super().update(instance, validated_data)
