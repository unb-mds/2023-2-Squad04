import json
from collections import defaultdict
from datetime import datetime

# Função para ler dados do novo formato de JSON
def ler_dados_novo_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados_json = json.load(arquivo_json)
    return dados_json

# Função para extrair dados do novo formato de JSON
def extrair_dados_novo_json(dados_pdf):
    contagem = defaultdict(lambda: defaultdict(int))

    for item in dados_pdf:
        municipio = item["Municipio"]
        pdf_data = item["Data"]
        mes = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%b")
        contagem[municipio][mes] += 1

    # Converter para o formato desejado e omitir entradas com "qtd": 0
    saida_json = [
        {"municipio": municipio, "mes": mes, "qtd": qtd}
        for municipio, meses in contagem.items()
        for mes, qtd in meses.items() if qtd > 0
    ]

    return saida_json

# Ler dados do novo formato de JSON de entrada
dados_pdf_novo_entrada = ler_dados_novo_json("data.json")

# Extrair dados do novo formato de JSON
saida_json_novo = extrair_dados_novo_json(dados_pdf_novo_entrada)

# Salvar em um arquivo JSON com codificação correta
with open("saida_novo_formato.json", "w", encoding="utf-8") as arquivo_saida:
    json.dump(saida_json_novo, arquivo_saida, indent=2, ensure_ascii=False)

print("Arquivo JSON gerado com sucesso.")
