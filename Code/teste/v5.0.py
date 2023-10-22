import re

# Função para filtrar palavras de uma linha
def filtrar_palavras(linha, palavras_chave):
    for palavra_chave in palavras_chave:
        # Usar expressão regular para encontrar a palavra-chave
        if re.search(r'\b{}\b'.format(re.escape(palavra_chave)), linha, re.IGNORECASE):
            return linha
    return None

# Nome do arquivo CSV de entrada
nome_arquivo_entrada = r"C:\Users\julii\OneDrive\Documentos\2023-2-Squad04\Code\teste\pdf.csv"
palavras_chave = ["valor", "reais", "R$", "cnpj", "objetivo"]  # Substitua com suas palavras-chave

# Nome do arquivo CSV de saída
nome_arquivo_saida = "exemplo_filtrado5.csv"

# Abra o arquivo de entrada e crie um arquivo de saída
with open(nome_arquivo_entrada, "r", encoding="utf-8") as arquivo_entrada, open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    # Processar cada linha do arquivo de entrada
    for linha in arquivo_entrada:
        nova_linha = filtrar_palavras(linha, palavras_chave)
        if nova_linha is not None:
            arquivo_saida.write(nova_linha)
