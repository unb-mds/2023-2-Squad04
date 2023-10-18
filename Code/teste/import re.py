import re

# Defina a expressão regular
pattern = r'(?<=,)\s*(?=,)|^(?=,)|[^\"]{2,}(?=\")|([^,\"]+(?=,|$))'

# Função para extrair valores de uma linha
def extrair_valores(linha):
    matches = re.findall(pattern, linha)
    return [match.strip() if match else "" for match in matches]

# Nome do arquivo CSV
nome_arquivo = "pdf.csv"

# Abra o arquivo CSV com o codec UTF-8
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    # Processar cada linha do arquivo
    for linha in arquivo:
        valores = extrair_valores(linha)
        print(valores)

