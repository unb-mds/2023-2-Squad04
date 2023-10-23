import json
import re
import csv

# Função para extrair informações específicas de uma linha
def extrair_informacoes(linha):
    informacoes = {
        "Município": None,
        "Objetivo": None,
        "Data": None,
        "Código": None,
        "Valor": None
    }

    # Expressão regular para extrair informações
    pattern = r'(?<=,)\s*(?=,)|^(?=,)|[^\"]{2,}(?=\")|([^,\"]+(?=,|$))'
    
    matches = re.findall(pattern, linha)
    
    if len(matches) >= 5:
        informacoes["Município"] = matches[0].strip()
        informacoes["Objetivo"] = matches[1].strip()
        informacoes["Data"] = matches[2].strip()
        informacoes["Código"] = matches[3].strip()
        informacoes["Valor"] = f"R$ {matches[4].strip()}"

    return informacoes

# Nome do arquivo CSV de entrada
nome_arquivo_entrada = r"C:\Users\julii\OneDrive\Documentos\2023-2-Squad04\dados.csv"

# Nome do arquivo JSON de saída
nome_arquivo_saida = "exemplo_filtrado10.json"

# Lista para armazenar as informações extraídas
informacoes_lista = []

# Abra o arquivo de entrada
with open(nome_arquivo_entrada, "r", encoding="utf-8") as arquivo_entrada:
    # Processar cada linha do arquivo de entrada
    for linha in arquivo_entrada:
        informacoes = extrair_informacoes(linha)
        if informacoes["Município"] is not None:
            informacoes_lista.append(informacoes)

# Salvar as informações em formato JSON
with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    json.dump(informacoes_lista, arquivo_saida, ensure_ascii=False, indent=4)