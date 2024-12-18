# models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome}"

class Gasto(models.Model):
    descricao = models.CharField(max_length=255)
    parcela = models.CharField(max_length=20, null=True, blank=True)
    valor = models.FloatField()
    valor_total = models.FloatField(null=True, blank=True)
    data = models.DateField()
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.valor} - {self.data}"
     