from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)

    # Campos de criação e atualização
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=20)
    ano = models.PositiveIntegerField()
    
    # Campos de criação e atualização
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"

    def __str__(self):
        return self.modelo

class Tarifa(models.Model):
    descricao = models.CharField(max_length=100, blank=True)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2)
    valor_diaria = models.DecimalField(max_digits=10, decimal_places=2)

    # Campos de criação e atualização
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Tarifa"
        verbose_name_plural = "Tarifas"

    def __str__(self):
        return self.descricao

class Estacionamento(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    tarifas = models.ManyToManyField(Tarifa)
    descricao = models.CharField(max_length=50, blank=True)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_saida = models.DateTimeField(null=True)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Campos adicionais (opcional)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('vencido', 'Vencido')], default='pendente')
    
    # Campos de criação e atualização
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    atualizado_em = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Estacionamento"
        verbose_name_plural = "Estacionamentos"

    def __str__(self):
        return self.descricao

