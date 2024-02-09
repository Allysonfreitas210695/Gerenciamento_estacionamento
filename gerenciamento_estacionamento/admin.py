from django.contrib import admin
from .models import Cliente, Veiculo, Tarifa, Estacionamento

admin.site.register(Cliente)
admin.site.register(Veiculo)
admin.site.register(Tarifa)
admin.site.register(Estacionamento)