import re
import json
from PyPDF2 import PdfFileReader

# Função para extrair informações específicas de uma linha
def extrair_informacoes(linha):
    informacoes = {
        "Município": None,
        "Objetivo": None,
        "Data": None,
        "Código": None,
        "Valor": None
    }

    # Expressões regulares para extrair informações específicas
    padrao_municipio = r'Município:\s*(.*?)$'
    padrao_objetivo = r'Objetivo:\s*(.*?)$'
    padrao_data = r'Data:\s*(\d{2}/\d{2}/\d{4})'
    padrao_codigo = r'Código:\s*(\d+)'
    padrao_valor = r'R\$\s*([0-9,.]+)'

    municipio = re.search(padrao_municipio, linha)
    objetivo = re.search(padrao_objetivo, linha)
    data = re.search(padrao_data, linha)
    codigo = re.search(padrao_codigo, linha)
    valor = re.search(padrao_valor, linha)

    if municipio:
        informacoes["Município"] = municipio.group(1).strip()
    if objetivo:
        informacoes["Objetivo"] = objetivo.group(1).strip()
    if data:
        informacoes["Data"] = data.group(1).strip()
    if codigo:
        informacoes["Código"] = codigo.group(1).strip()
    if valor:
        informacoes["Valor"] = f"R$ {valor.group(1).strip()}"

    return informacoes

# Nome do arquivo PDF de entrada
nome_arquivo_pdf = r"C:\Code\teste\test.pdf"

# Nome do arquivo JSON de saída
nome_arquivo_saida = "exemplo_filtrado8.json"

# Lista para armazenar as informações extraídas
informacoes_lista = []

# Abra o arquivo PDF de entrada
with open(nome_arquivo_pdf, "rb") as arquivo_pdf:
    pdf_reader = PdfFileReader(arquivo_pdf)

    # Iterar por todas as páginas do PDF
    for pagina_numero in range(pdf_reader.numPages):
        pagina = pdf_reader.getPage(pagina_numero)
        texto = pagina.extractText()

        # Dividir o texto em linhas
        linhas = texto.split('\n')

        # Processar cada linha do PDF
        for linha in linhas:
            informacoes = extrair_informacoes(linha)
            if informacoes["Município"] is not None:
                informacoes_lista.append(informacoes)

# Salvar as informações em formato JSON
with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    json.dump(informacoes_lista, arquivo_saida, ensure_ascii=False, indent=4)
