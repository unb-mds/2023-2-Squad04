import re

# Função para filtrar palavras de uma linha
def filtrar_palavras(linha, palavra_chave):
    # Usar expressão regular para encontrar a palavra-chave
    ocorrencias = re.finditer(r'\b{}\b'.format(re.escape(palavra_chave)), linha, re.IGNORECASE)

    # Retornar as ocorrências encontradas
    return [ocorrencia.group() for ocorrencia in ocorrencias]

# Nome do arquivo CSV
nome_arquivo = "pdf.csv"
palavra_chave = "nomeação"  # Substitua "exemplo" pela palavra que deseja filtrar

# Abra o arquivo CSV com o codec UTF-8
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    # Processar cada linha do arquivo
    for linha in arquivo:
        palavras_filtradas = filtrar_palavras(linha, palavra_chave)
        if palavras_filtradas:
            print(palavras_filtradas)
