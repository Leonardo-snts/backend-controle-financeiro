# views.py
import logging
from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Gasto, Pessoa
from .serializers import PessoaSerializer, GastoSerializer, UploadPDFSerializer
from service.ia import process_file
import pandas as pd
import pdfplumber
import re
import os

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer

    @action(detail=False, methods=['post'])
    def upload_pdf(self, request):
        serializer = UploadPDFSerializer(data=request.data)
        if serializer.is_valid():
            pdf = request.FILES['pdf']
            fs = FileSystemStorage()
            filename = fs.save(pdf.name, pdf)
            file_url = fs.url(filename)

            # Processa o PDF
            try:
                with pdfplumber.open(pdf) as pdf_file:
                    dados_gastos = []

                    # Expressões regulares para identificar padrões
                    date_pattern = r"\d{2}/\d{2}/\d{4}"  # Padrão de datas no formato DD/MM/AAAA
                    value_pattern = r"\d+[\.,]?\d*"       # Padrão de valores monetários
                    parcela_pattern = r"parcela (\d+)/(\d+)"  # Exemplo: "parcela 2/10"

                    for page in pdf_file.pages:
                        text = page.extract_text()  # Extrai o texto da página
                        lines = text.split("\n")  # Divide em linhas

                        for line in lines:
                            # Busca padrões na linha
                            date_match = re.search(date_pattern, line)
                            value_match = re.search(value_pattern, line)
                            parcela_match = re.search(parcela_pattern, line)

                            # Extrai informações da linha
                            data = date_match.group() if date_match else None
                            valor = value_match.group() if value_match else None
                            parcela = parcela_match.groups() if parcela_match else (None, None)

                            # Parte restante como descrição
                            descricao = line.replace(data, "").replace(valor, "").strip() if data and valor else line.strip()

                            # Adiciona ao conjunto de dados se houver valor
                            if valor:
                                dados_gastos.append({
                                    'data': data,
                                    'descricao': descricao,
                                    'valor': valor,
                                    'parcela_atual': parcela[0],
                                    'total_parcelas': parcela[1]
                                })

                    # Converte os dados em um DataFrame para análises futuras
                    df = pd.DataFrame(dados_gastos)

                    # Exemplo: salvar o DataFrame em um arquivo CSV (opcional)
                    df.to_csv("gastos_extratos.csv", index=False)

                    print(df)  # Inspecione os dados no console

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"file_url": file_url, "dados": dados_gastos}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdicionarPessoaView(APIView):
    def post(self, request):
        nome = request.data.get('nome')
        email = request.data.get('email')

        if not nome or not email:
            return Response({"error": "Nome e email são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        pessoa = Pessoa.objects.create(nome=nome, email=email)
        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProcessFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        temp_file_path = None  # Inicializar a variável
        try:
            logging.info(f"Request FILES: {request.FILES.keys()}")  # Log para verificar os arquivos enviados

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

            # Retornar os dados processados
            return Response(processed_data.to_dict(orient='records'), status=status.HTTP_200_OK)

        except Exception as e:
            logging.error(f"Erro ao processar o arquivo: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            # Remover o arquivo temporário, se existir
            if temp_file_path and os.path.exists(temp_file_path):
                os.remove(temp_file_path)
    
    def debug_middleware(get_response):
        def middleware(request):
            print("REQUEST CONTENT-TYPE:", request.content_type)
            print("FILES RECEBIDOS:", request.FILES)
            print("POST DATA:", request.POST)
            response = get_response(request)
            return response
        return middleware
