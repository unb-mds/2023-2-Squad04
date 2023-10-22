import re

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
    padrao_municipio = r'Município:\s*(.*?)'
    padrao_objetivo = r'Objetivo:\s*(.*?)'
    padrao_data = r'Data:\s*(\d{2}/\d{2}/\d{4})'
    padrao_codigo = r'Código:\s*(\d+)'
    padrao_valor = r'Valor:\s*(R\$\s*[0-9,.]+)'

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
        informacoes["Valor"] = valor.group(1).strip()

    return informacoes

# Nome do arquivo de entrada
nome_arquivo_entrada = "Code\teste\pdf.csv"

# Nome do arquivo de saída
nome_arquivo_saida = "exemplo_filtrado6.csv"

# Abra o arquivo de entrada e crie um arquivo de saída
with open(nome_arquivo_entrada, "r", encoding="utf-8") as arquivo_entrada, open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    # Processar cada linha do arquivo de entrada
    for linha in arquivo_entrada:
        informacoes = extrair_informacoes(linha)
        if informacoes["Município"] is not None:
            arquivo_saida.write(f"Município: {informacoes['Município']}\n")
            arquivo_saida.write(f"Objetivo: {informacoes['Objetivo']}\n")
            arquivo_saida.write(f"Data: {informacoes['Data']}\n")
            arquivo_saida.write(f"Código: {informacoes['Código']}\n")
            arquivo_saida.write(f"Valor: {informacoes['Valor']}\n\n")
