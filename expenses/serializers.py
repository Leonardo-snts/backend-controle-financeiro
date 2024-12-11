# serializers.py
from rest_framework import serializers
from .models import  Pessoa, ProcessedData

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email']

class ProcessedDataSerializer(serializers.ModelSerializer):
    pessoa = serializers.CharField(source='pessoa.nome', read_only=True)
     
    class Meta:
        model = ProcessedData
        fields = ['id', 'descricao', 'parcela', 'valor', 'data', 'pessoa']
