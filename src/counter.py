from collections import defaultdict
from datetime import datetime
import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def ler_dados_novo_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados_json = json.load(arquivo_json)
    return dados_json

def extrair_dados_novo_json(dados_pdf):
    contagem = defaultdict(lambda: defaultdict(int))

    for item in dados_pdf:
        municipio = item["Municipio"]
        pdf_data = item["Data"]

        # Extrair o ano e o mês da data
        ano = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%Y")
        mes = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%b")

        # Incrementar as contagens corretamente
        contagem[municipio][(ano, mes)] += 1

    # Criar a lista de saída com todas as combinações de municípios, meses e anos
    saida_lista = []
    soma_todos = defaultdict(int)

    for municipio, contagens_municipio in contagem.items():
        for (ano, mes), qtd in sorted(contagens_municipio.items(), key=lambda x: (x[0][0], datetime.strptime(x[0][1], "%b").month)):
            saida_lista.append({"municipio": municipio, "mes": mes, "ano": ano, "qtd": qtd})
            soma_todos[(ano, mes)] += qtd

    # Adicionar entrada para "Todos"
    for (ano, mes), qtd_total in sorted(soma_todos.items(), key=lambda x: (x[0][0], datetime.strptime(x[0][1], "%b").month)):
        saida_lista.append({"municipio": "Todos", "mes": mes, "ano": ano, "qtd": qtd_total})

    return saida_lista

dados_pdf_novo_entrada = ler_dados_novo_json(diretorio_atual + "/dados/data.json")
saida_lista_nova = extrair_dados_novo_json(dados_pdf_novo_entrada)

# Escrever no arquivo
with open(diretorio_atual + "/dados/counter.json", "w", encoding="utf-8") as arquivo_saida:
    json.dump(saida_lista_nova, arquivo_saida, indent=2, ensure_ascii=False)

print("Arquivo JSON gerado com sucesso.")
