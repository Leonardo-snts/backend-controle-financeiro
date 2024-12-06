import requests

url = "http://localhost:8000/api/process-file/"
file_path = "/home/leonardo-dev/projetos/gastos/backend-gastos/media/treino/teste_aleatorio.xlsx"

with open(file_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)
    
if response.status_code == 200:
    data = response.json()
    for item in data:
        print(item) 
else:
    print("Erro:", response.json())

print("Status code:", response.status_code)
print("Response:", response.json())