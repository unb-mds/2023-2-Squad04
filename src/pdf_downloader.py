import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime, timedelta

def obter_ultima_data():
    try:
        with open('pdf_downloader_last_date.txt', 'r') as file:
            data_str = file.read().strip()
            if data_str:
                return datetime.strptime(data_str, '%Y-%m-%d')
    except FileNotFoundError:
        pass
    return datetime(2023, 1, 1)

def salvar_ultima_data(data):
    with open('pdf_downloader_last_date.txt', 'w') as file:
        file.write(data.strftime('%Y-%m-%d'))

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

download_dir = diretorio_atual + "/pdfs"



options = webdriver.ChromeOptions()

options.binary_location = "/usr/bin/google-chrome"
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

options.add_experimental_option('prefs', {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True 
})

driver = webdriver.Chrome(options=options)

link_base = "https://www.diariomunicipal.com.br/famup/"

driver.get(link_base)

months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

ultima_data = obter_ultima_data()
data_atual = datetime.now()

for y in range(ultima_data.year, data_atual.year + 1):
    year = driver.find_element(By.ID, "calendar_year")
    year.click()

    selected_year = driver.find_element(By.XPATH, f"//option[text()='{y}']")
    selected_year.click()

    start_month_index = ultima_data.month - 1 if y == ultima_data.year else 0  # índice do mês diretamente através do valor presente no arquivo

    for m in range(start_month_index, len(months)) if y < data_atual.year else range(start_month_index, data_atual.month):
        month = driver.find_element(By.ID, "calendar_month")
        month.click()

        selected_month = driver.find_element(By.XPATH, f"//option[text()='{months[m]}']")
        selected_month.click()

        inicio_dia = ultima_data.day+1 if m == start_month_index and y == ultima_data.year else 1

        for i in range(inicio_dia,33):
            if i > data_atual.day and ultima_data.month == data_atual.month:
                break
            try:
                day = driver.find_element(By.ID, "calendar_day")
                day.click()
                sleep(0.5)
                selected_day = driver.find_element(By.XPATH, f"//option[text()='{i}']")
                selected_day.click()

            except:
                break

            sleep(0.1)
            clickable = driver.find_element(By.CLASS_NAME, "selected")
            clickable.click()

            sleep(1.5)

            verificar = False
            try:
                pdf_link = driver.find_element(By.ID, "btDownloadSimples2")
                pdf_link.click()
                print(f'Diário do dia {i}/{months[m]}/{y} encontrado!')

            except:
                verificar = True

            try:
                if verificar:
                    pdf_link = driver.find_element(By.ID, "btDownloadSimples")
                    pdf_link.click()
                    print(f'Diário do dia {i}/{months[m]}/{y} encontrado!')

            except:
                print(f"Diário do dia {i}/{months[m]}/{y} não encontrado!")

            sleep(0.2)
            close = driver.find_element(By.CLASS_NAME, "bt-fechar")
            close.click()
            sleep(0.2)

nova_ultima_data = datetime.now()
salvar_ultima_data(nova_ultima_data)
