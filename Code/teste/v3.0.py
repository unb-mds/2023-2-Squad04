import re

# Função para filtrar palavras de uma linha
def filtrar_palavras(linha, palavras_chave):
    palavras_filtradas = []

    for palavra_chave in palavras_chave:
        # Usar expressão regular para encontrar a palavra-chave
        ocorrencias = re.finditer(r'\b{}\b'.format(re.escape(palavra_chave)), linha, re.IGNORECASE)

        # Adicionar as ocorrências à lista de palavras filtradas
        palavras_filtradas.extend([ocorrencia.group() for ocorrencia in ocorrencias])

    return palavras_filtradas

# Nome do arquivo CSV
nome_arquivo = "pdf.csv"
palavras_chave = ["caaporã", "valor"]  # Substitua com suas palavras-chave

# Abra o arquivo CSV com o codec UTF-8
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    # Processar cada linha do arquivo
    for linha in arquivo:
        palavras_filtradas = filtrar_palavras(linha, palavras_chave)
        if palavras_filtradas:
            print(palavras_filtradas)
