# serializers.py
from rest_framework import serializers
from .models import Gasto, Pessoa
from rest_framework.fields import FileField

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'email']

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = ['id', 'pessoa', 'valor', 'descricao', 'data', 'categoria']

class UploadPDFSerializer(serializers.Serializer):
    pdf = FileField()

    def validate_pdf(self, value):
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("O arquivo deve ser um PDF.")
        return value
