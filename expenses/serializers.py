# serializers.py
from rest_framework import serializers
from .models import  Pessoa, Gasto
from django.db import models

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email']

class GastoSerializer(serializers.ModelSerializer):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
     
    class Meta:
        model = Gasto
        fields = ['id', 'descricao', 'parcela', 'valor', 'pessoa', 'data']
