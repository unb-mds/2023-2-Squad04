import re
import json
import PyPDF2

# Função para extrair informações específicas de uma linha
def extrair_informacoes(linha, informacoes):
    for chave, padrao in informacoes_padroes.items():
        match = re.search(padrao, linha)
        if match:
            informacoes[chave] = match.group(1).strip() if match.group(1) else None

# Expressões regulares para capturar informações-chave
informacoes_padroes = {
    "CONTRATANTE": r'CONTRATANTE: (.+)',
    "CONTRATADA": r'CONTRATADA: (.+)',
    "OBJETO": r'OBJETO: (.+)',
    "VALOR GLOBAL": r'VALOR GLOBAL: (.+)',
    "PRAZO": r'PRAZO: (.+)',
    "Data": r'(\d+ de [A-Za-z]+ de \d+)',
    "Presidente": r'(.+)\n(.+)',
    "Código Identificador": r'Código Identificador:(.+)',
    "RG": r'RG nº (.+),',
    "CPF": r'CPF nº (.+),',
    "Órgão": r'Órgão: (.+)',
    "Tipo": r'Tipo: (.+)',
    "Instrumento": r'INSTRUMENTO: (.+)',
    "CNPJ": r'cadastrada no CNPJ\nnº (.+).',
    "Objeto Licitação": r'OBJETO: (.+)',
    "Pregoeira": r'PREGOEIRA OFICIAL DO MUNICÍPIO DE (.+)',
    "Data Licitação": r'(\d+ de [A-Za-z]+ de \d+)',
    "Assinatura Pregoeira": r'(.+)\n(.+)'
}

# Nome do arquivo PDF de entrada
nome_arquivo_pdf = r"Code\teste\publicado_17460_2013-11-12_3ea8fd446e5cf648db214850cfb6c514.pdf"

# Nome do arquivo JSON de saída
nome_arquivo_saida = "informacoes_extraidas3.json"

# Inicializar a lista para armazenar as informações extraídas
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
        if any(informacoes.values()):
            informacoes_lista.append(informacoes)

# Salvar as informações em formato JSON
with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
    json.dump(informacoes_lista, arquivo_saida, ensure_ascii=False, indent=4)
