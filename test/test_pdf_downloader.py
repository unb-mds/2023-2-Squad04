import os
import shutil
import pytest
from src.pdf_downloader import obter_ultima_data, salvar_ultima_data, configurar_driver, lidar_com_mensagem_manutencao, processar_dias
from datetime import datetime, timedelta
from time import sleep

@pytest.fixture
def driver():
    return configurar_driver()

def test_baixar_pdfs(driver):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(diretorio_atual, "..", "src", "pdfs/")
    print(f"Caminho absoluto do diretório de downloads: {os.path.abspath(download_dir)}")

    # Configurações para download
    options = driver

    link_base = "https://www.diariomunicipal.com.br/famup/"
    driver.get(link_base)

    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    ultima_data = obter_ultima_data()
    data_atual = datetime.now() 

    lidar_com_mensagem_manutencao(driver)
    processar_dias(driver, ultima_data, data_atual, months)

    sleep(5)
    print(f"Caminho absoluto do diretório de downloads: {os.path.abspath(download_dir)}")
    print(f"Conteúdo do diretório de downloads: {os.listdir(download_dir)}")
    pdfs_encontrados = [f for f in os.listdir(download_dir) if f.endswith(".pdf")]
    assert pdfs_encontrados, "Nenhum PDF foi encontrado."


    pdfs_encontrados = [f for f in os.listdir(download_dir) if f.endswith(".pdf")]
    assert pdfs_encontrados, "Nenhum PDF foi encontrado."

    nova_ultima_data = datetime.now()
    salvar_ultima_data(nova_ultima_data)

if __name__ == "__main__":
    pytest.main()
