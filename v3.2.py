import re
import json
import logging
from PyPDF2 import PdfReader
import requests
from io import BytesIO

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

# Função para extrair informações específicas de uma linha
def extrair_informacoes(linha, informacoes):
    for chave, padrao in informacoes_padroes.items():
        match = re.search(padrao, linha)
        if match:
            informacoes[chave] = match.group(1).strip() if match.group(1) else None

# Função para processar uma página do PDF
def processar_pagina(pagina):
    informacoes = {}
    for linha in pagina.extract_text().split('\n'):
        extrair_informacoes(linha, informacoes)
    return informacoes

def extrair_informacoes_pdf(url_pdf):
    try:
        response = requests.get(url_pdf)
        response.raise_for_status()

        pdf_content = BytesIO(response.content)
        pdf_reader = PdfReader(pdf_content)

        informacoes_lista = []

        for pagina_num in range(len(pdf_reader.pages)):
            pagina = pdf_reader.pages[pagina_num]
            informacoes = processar_pagina(pagina)
            if any(informacoes.values()):
                informacoes_lista.append(informacoes)

        return informacoes_lista

    except requests.exceptions.RequestException as e:
        logging.error("Erro ao fazer a requisição HTTP: %s", e)
        return []

    except Exception as e:
        logging.error("Erro inesperado: %s", e)
        return []

def salvar_em_json(informacoes_lista, nome_arquivo_saida):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo_saida:
        json.dump(informacoes_lista, arquivo_saida, ensure_ascii=False, indent=4)

def main():
    url_pdf = "https://auniao.pb.gov.br/servicos/doe/2023/novembro/diario-oficial-29-11-2023.pdf"
    nome_arquivo_saida = "exemplo_filtrado.json"

    informacoes_lista = extrair_informacoes_pdf(url_pdf)
    salvar_em_json(informacoes_lista, nome_arquivo_saida)

    logging.info("Extração concluída com sucesso. Dados salvos em %s", nome_arquivo_saida)

if __name__ == "__main__":
    main()
