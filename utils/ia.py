import pandas as pd
import logging
import os
import unidecode

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Função para processar Excel ou CSV
def process_file(file_path):
    try:
        # Verificar a extensão do arquivo
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension == ".csv":
            logging.info(f"Carregando arquivo CSV: {file_path}")
            data = pd.read_csv(file_path)

        elif file_extension == ".xlsx":
            logging.info(f"Carregando arquivo Excel: {file_path}")
            data = pd.read_excel(file_path)

        else:
            raise ValueError("Arquivo deve ser CSV ou Excel.")

        # Exibir o conteúdo original do arquivo
        logging.info(f"Conteúdo original do arquivo:\n{data.head()}")

        # Padronizar os nomes das colunas para evitar problemas com acentuação e diferenças de nome
        normalized_columns = {
            unidecode.unidecode(col).lower(): col for col in data.columns
        }

        # Mapear as colunas necessárias
        required_columns = {
            "descricao": None,
            "parcela": None,
            "valor": None,
            "data": None
        }

        # Procurar pelas colunas no arquivo
        for key in required_columns:
            for normalized, original in normalized_columns.items():
                if key in normalized:
                    required_columns[key] = original

        # Verificar se todas as colunas obrigatórias foram encontradas
        if None in required_columns.values():
            missing_columns = [key for key, value in required_columns.items() if value is None]
            raise ValueError(f"Colunas faltando no arquivo: {', '.join(missing_columns)}")

        # Filtrando apenas as colunas relevantes
        data = data[list(required_columns.values())]
        data.columns = list(required_columns.keys())  # Renomeando as colunas

        # Verificar e padronizar formatos de data e valores
        logging.info("Padronizando formatos de datas e valores.")
        data["data"] = pd.to_datetime(data["data"], errors="coerce")

        # Tratar valores numéricos e strings corretamente na coluna 'valor'
        if data["valor"].dtype == "O":  # Verifica se a coluna 'valor' contém objetos (strings)
            data["valor"] = data["valor"].str.replace("R\$ ", "").str.replace(",", ".")
        data["valor"] = pd.to_numeric(data["valor"], errors="coerce")  # Conversão de valores para numéricos

        # Exibir o DataFrame após a conversão de dados
        logging.info(f"Conteúdo após a padronização de dados:\n{data.head()}")

        logging.info("Dados processados com sucesso.")
        return data

    except Exception as e:
        logging.error(f"Erro ao processar o arquivo: {e}")
        raise

# Exemplo de uso
if __name__ == "__main__":
    # Caminho do arquivo a ser processado (pode ser CSV ou Excel)
    file_path = "/home/leonardo-dev/projetos/gastos/backend-gastos/media/treino/teste_aleatorio.xlsx"  # Exemplo de caminho de arquivo

    try:
        # Processar o arquivo
        processed_data = process_file(file_path)
        print("Dados processados:\n", processed_data)
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
