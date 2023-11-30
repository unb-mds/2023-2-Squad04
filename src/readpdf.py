from PyPDF2 import PdfReader
import re
import json
import codecs
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(diretorio_atual, 'lista_pdfs.txt')

pdf_path = os.path.join(diretorio_atual, 'pdfs')

save_path = os.path.join(diretorio_atual, 'dados')

#nome da lista com os arquivos de pdf
linhas = []

with open(nome_arquivo, "r", encoding="utf-8") as arquivo_txt:
    linhas = arquivo_txt.readlines()
    
for i in range(len(linhas)):
    pdf_name = linhas[i].strip()

    reader = PdfReader(f'{pdf_path}/{pdf_name}')
    number_of_pages = len(reader.pages)
    dados = {}

    for i in range(number_of_pages):
        n_page = i

        page = reader.pages[n_page]
        text = page.extract_text()

        print("Página: ", n_page)

        padrao = r'COMISSÃO DE LICITAÇÃO(.*?)Código Identificador: (\w+)'

        resultados = re.findall(padrao, text, re.DOTALL)

        if (resultados == []):
            padrao = r'COMISSÃO DE LICITAÇÃ O(.*?)Código Identificador: (\w+)'
            resultados = re.findall(padrao, text, re.DOTALL)
            
        for resultado in resultados:
            print("Dado encontrado!")
            
            texto_encontrado = resultado[0].strip()
            codigo_identificador = resultado[1]
            
            #Extrair Codigo
            dados_json = [{
                "Titulo PDF": pdf_name,
                "Texto encontrado:": texto_encontrado,
                "Código identificador": codigo_identificador 
            }]
            
            with open(f'{save_path}/data.json', 'r', encoding="utf-8") as arquivo_json:
                old_json = json.load(arquivo_json)
            
            old_json.append(dados_json)
            
            with open(f'{save_path}/data.json', "w", encoding="utf-8") as arquivo_json:
                json.dump(old_json, arquivo_json, ensure_ascii=False,indent=2) 