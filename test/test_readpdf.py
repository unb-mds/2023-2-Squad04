import os
import json
import pytest
from src.pdf_downloader import obter_ultima_data, salvar_ultima_data, configurar_driver, lidar_com_mensagem_manutencao, processar_dias
from PyPDF2 import PdfReader
from datetime import datetime

@pytest.fixture
def configurar_ambiente():

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(diretorio_atual,'..','src', 'lista_pdfs.txt')
    pdf_path = os.path.join(diretorio_atual,'..','src', 'pdfs')
    save_path = os.path.join(diretorio_atual,'..','src', 'dados')

    yield

def test_processar_pdf(configurar_ambiente):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(diretorio_atual,'..','src', 'lista_pdfs.txt')
    pdf_path = os.path.join(diretorio_atual,'..','src', 'pdfs')
    save_path = os.path.join(diretorio_atual,'..','src', 'dados')


    with open(f'{save_path}/data.json', 'r', encoding="utf-8") as arquivo_json:
        dados_json = json.load(arquivo_json)

    assert len(dados_json) > 0
    assert 'Titulo_PDF' in dados_json[0]
    assert 'Texto_encontrado' in dados_json[0]
    assert 'Codigo_identificador' in dados_json[0]
    assert 'Data' in dados_json[0]
    assert 'Municipio' in dados_json[0]
