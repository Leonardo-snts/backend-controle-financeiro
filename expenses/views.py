# views.py
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .models import ProcessedData, Pessoa
from .serializers import PessoaSerializer, ProcessedDataSerializer
from service.ia import process_file
import os
import logging
import numpy as np

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class AdicionarPessoaView(APIView):
    def post(self, request):
        nome = request.data.get('nome')
        email = request.data.get('email')

        if not nome or not email:
            return Response({"error": "Nome e email são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        pessoa = Pessoa.objects.create(nome=nome, email=email)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    
class ProcessedDataViewSet(viewsets.ModelViewSet):
    queryset = ProcessedData.objects.all()
    serializer_class = ProcessedDataSerializer

class ProcessFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        temp_file_path = None
        try:
            logging.info(f"Request FILES: {request.FILES.keys()}")  # Log para verificar arquivos enviados

            # Obter o arquivo enviado
            uploaded_file = request.FILES.get('file')
            if not uploaded_file:
                return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)

            logging.info(f"Arquivo recebido: {uploaded_file.name}")

            # Salvar o arquivo temporariamente
            temp_file_path = f"/tmp/{uploaded_file.name}"
            with open(temp_file_path, 'wb+') as temp_file:
                for chunk in uploaded_file.chunks():
                    temp_file.write(chunk)

            # Processar o arquivo
            processed_data = process_file(temp_file_path)

            # Substituir valores NaN por None
            processed_data = processed_data.replace({np.nan: None})

            # Salvar os dados processados no banco
            saved_records = []
            for record in processed_data.to_dict(orient='records'):
                # Criar a instância do modelo e salvar
                obj = ProcessedData.objects.create(**record)
                saved_records.append(obj.id)

            # Retornar os IDs dos registros salvos e os dados processados
            return Response({
                "message": "Dados processados e salvos com sucesso.",
                "saved_ids": saved_records,
                "data": processed_data.to_dict(orient='records'),
            }, status=status.HTTP_200_OK)

        except Exception as e:
            logging.error(f"Erro ao processar o arquivo: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            # Remover o arquivo temporário, se existir
            if temp_file_path and os.path.exists(temp_file_path):
                os.remove(temp_file_path)
