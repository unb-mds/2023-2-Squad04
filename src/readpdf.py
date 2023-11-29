from PyPDF2 import PdfReader
import re
import json
import codecs

#nome da lista com os arquivos de pdf
nome_arquivo = "lista_pdfs.txt"
linhas = []

with open(nome_arquivo, "r", encoding="utf-8") as arquivo_txt:
    linhas = arquivo_txt.readlines()
    
for i in range(len(linhas)):
    pdf_name = linhas[i].strip()

    reader = PdfReader(pdf_name)
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

        j = 0
        for resultado in resultados:
            texto_encontrado = resultado[0].strip()
            codigo_identificador = resultado[1]
            print("-" * 100)
            print(texto_encontrado)
            j += 1
            #Extrair Codigo
            print("Código Identificador:", codigo_identificador)
            dados[codigo_identificador] = texto_encontrado
            
    #as informações de cada pdf serão salvas em um arquivo com o mesmo nome do pdf mas com a extensão JSON
    nome_arquivo = f"{pdf_name}.json"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False,indent=2) 