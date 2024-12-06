# serializers.py
from rest_framework import serializers
from .models import  Pessoa, ProcessedData

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email']

class ProcessedDataSerializer(serializers.ModelSerializer):
    pessoa = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all(), required=False)
    #pessoas_divididas = serializers.PrimaryKeyRelatedField(queryset=Pessoa.objects.all(), many=True, required=False)

    class Meta:
        model = ProcessedData
        fields = ['id', 'descricao', 'parcela', 'valor', 'data', 'pessoa']
