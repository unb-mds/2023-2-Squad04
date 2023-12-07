import json
from collections import defaultdict
from datetime import datetime
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Função para ler dados do novo formato de JSON
def ler_dados_novo_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados_json = json.load(arquivo_json)
    return dados_json

# Função para extrair dados do novo formato de JSON
def extrair_dados_novo_json(dados_pdf):
    contagem = defaultdict(lambda: defaultdict(int))
    total_todos = defaultdict(int)

    saida_json = []

    for item in dados_pdf:
        municipio = item["Municipio"]
        pdf_data = item["Data"]

        # Extrair o mês e o ano da data
        mes = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%b")
        ano = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%Y")

        contagem[municipio][mes] += 1
        total_todos[mes] += 1

        saida_json.append({"municipio": municipio, "mes": mes, "qtd": 1, "ano": ano})

    return saida_json

# Ler dados do novo formato de JSON de entrada
dados_pdf_novo_entrada = ler_dados_novo_json(diretorio_atual + "/dados/data.json")

# Extrair dados do novo formato de JSON
saida_json_novo = extrair_dados_novo_json(dados_pdf_novo_entrada)

# Salvar em um arquivo JSON com codificação correta
with open(diretorio_atual + "/dados/counter.json", "w", encoding="utf-8") as arquivo_saida:
    json.dump(saida_json_novo, arquivo_saida, indent=2, ensure_ascii=False)

print("Arquivo JSON gerado com sucesso.")
