# models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Gasto(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data = models.DateField()
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.descricao} - {self.valor} - {self.data}"
