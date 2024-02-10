from django.contrib.auth.models import User
from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator

# Create your models here.
class Profile(models.Model):
    PERFIL_CHOICES = [
        ('admin', 'Admin')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    nome = models.CharField(max_length=120, null=False, blank=False)
    email = models.EmailField(unique=True, validators=[EmailValidator("Informe um endereço de e-mail válido.")], blank=False, null=False)
    senha = models.CharField(max_length=30, validators=[MinLengthValidator(limit_value=6, message="A senha deve ter pelo menos 6 caracteres.")], null=False, blank=False)
    perfil = models.CharField(max_length=20, choices=PERFIL_CHOICES, default='admin')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.nome