import re
import json
import PyPDF2

def extrair_informacoes(linha, informacoes):
    for chave, padrao in informacoes_padroes.items():
        match = re.search(padrao, linha)
        try:
            if match:
                informacoes[chave] = match.group(1).strip()
            else:
                informacoes[chave] = None
        except IndexError:
            informacoes[chave] = None



# Expressões regulares para capturar informações-chave
informacoes_padroes = {
    "Órgão": r'Órgão: (.+)',
    "Tipo": r'Tipo: (.+)',
    "Instrumento": r'Instrumento: (.+)',
    "Contratante": r'CONTRATANTE: (.+)',
    "Contratada": r'CONTRATADA: (.+)',
    "CNPJ": r'CNPJ: (.+)',
    "Objeto": r'OBJETO: (.+)',
    "Valor Mensal": r'Valor Mensal: (.+)',
    "Valor Global": r'VALOR GLOBAL: (.+)',
    "Prazo": r'PRAZO: (.+)',
    "Data": r'(\d+ de [A-Za-z]+ de \d+)',
    "Assinatura": r'(.+)\n(.+)',
    "Portaria": r'PORTARIA Nº (\d+/\d+)',
    "Instituto": r'INSTITUTO DE PREVIDÊNCIA SOCIAL DOS SERVIDORES MUNICIPAIS DE CAAPORÃ \(IPSEC\)',
    "Nomeação": r'Nomear o Sr. (.+), RG nº (.+), CPF nº (.+),',
    "Objeto Licitação": r'OBJETO: (.+)',
    "Pregoeira": r'PREGOEIRA OFICIAL DO MUNICÍPIO DE CAAPORÃ',
    "Data Licitação": r'(\d+ de [A-Za-z]+ de \d+)',
    "Assinatura Pregoeira": r'(.+)\n(.+)'

}

# Nome do arquivo PDF de entrada
nome_arquivo_pdf = r"Code\teste\test.pdf"

# Nome do arquivo JSON de saída
nome_arquivo_saida = "informacoes_extraidas2.json"

# Lista para armazenar as informações extraídas
informacoes_lista = []

# Abrir o arquivo PDF
with open(nome_arquivo_pdf, "rb") as arquivo_pdf:
    pdf_reader = PyPDF2.PdfReader(arquivo_pdf)

    # Extrair o texto de cada página do PDF
    for pagina_num in range(len(pdf_reader.pages)):
        pagina = pdf_reader.pages[pagina_num]
        texto = pagina.extract_text()

        # Inicializar um dicionário para armazenar as informações desta página
        informacoes = {}

        # Processar cada linha do texto extraído
        for linha in texto.split('\n'):
            extrair_informacoes(linha, informacoes)

        # Adicionar as informações extraídas à lista
        if informacoes:
            informacoes_lista.append(informacoes)

# Salvar as informações em formato JSON
with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    json.dump(informacoes_lista, arquivo_saida, ensure_ascii=False, indent=4)
