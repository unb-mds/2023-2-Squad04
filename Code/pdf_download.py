from selenium import webdriver
import time 

download_dir = "C:\\..." #coloque o caminho onde você deseja que o download seja feito

options = webdriver.ChromeOptions()

#Nessa parte as configurações do chrome são alteradas para que o download seja realizado assim que a página for aberta
options.add_experimental_option('prefs', {
"download.default_directory": download_dir,
"download.prompt_for_download": False, 
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True 
})

driver = webdriver.Chrome(options=options) 

link_base = 'https://iose.se.gov.br/apifront/portal/edicoes/pdf_diario/'
#O range do for deve ser as páginas que você deseja acessar
#Caso a página não esteja carregando rápido o suficiente você pode mudar o time.sleep
for i in range(5492, 5494):
    driver.get(f'{link_base}{i}')
    time.sleep(10)
