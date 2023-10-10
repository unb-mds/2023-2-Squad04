#Em caso de erro é necessário manipular o sleep, pois depende da velocidade da sua internet

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys
from time import sleep

download_dir = "/" #coloque o caminho onde você deseja que o download seja feito

options = webdriver.ChromeOptions()

#Nessa parte as configurações do chrome são alteradas para que o download seja realizado assim que a página for aberta
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

for y in range(2010, 2024):
    year = driver.find_element(By.ID, "calendar_year")
    year.click()

    selected_year = driver.find_element(By.XPATH,f"//option[text()='{y}']")
    selected_year.click()
    for m in months:
        month = driver.find_element(By.ID, "calendar_month")
        month.click()

        selected_month = driver.find_element(By.XPATH,f"//option[text()='{m}']")
        selected_month.click()

        for i in range(1,33):
            try:
                day = driver.find_element(By.ID, "calendar_day")
                day.click()
                sleep(0.5)
                selected_day = driver.find_element(By.XPATH,f"//option[text()='{i}']")
                selected_day.click()

            except:
                break

            sleep(0.1)
            clickable = driver.find_element(By.CLASS_NAME, "selected")
            clickable.click()

            sleep(1.5)

            verificar =False
            try:
                pdf_link = driver.find_element(By.ID, "btDownloadSimples2")
                pdf_link.click()
                print(f'Diário do dia {i}/{m}/{y} encontrado!')

            except:
                verificar = True 

            try:
                if verificar:
                    pdf_link = driver.find_element(By.ID, "btDownloadSimples")
                    pdf_link.click()
                    print(f'Diário do dia {i}/{m}/{y} encontrado!')
            
            except:
                print(f"Diário do dia {i}/{m}/{y} não encontrado!")


            sleep(0.2)
            close = driver.find_element(By.CLASS_NAME, "bt-fechar")
            close.click()
            sleep(0.2)