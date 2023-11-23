from PyPDF2 import PdfReader
import re

pdf_name = ""
reader = PdfReader(pdf_name)
number_of_pages = len(reader.pages)
dados = {}

for i in range(number_of_pages):
    n_page = i

    dados['pagina'] = n_page

    page = reader.pages[n_page]
    text = page.extract_text()

    print("Página: ", n_page)

    padrao = r'COMISSÃO DE LICITAÇÃO(.*?)Código Identificador: (\w+)'

    resultados = re.findall(padrao, text, re.DOTALL)

    j = 0
    for resultado in resultados:
        texto_encontrado = resultado[0].strip()
        codigo_identificador = resultado[1]
        print("-" * 100)
        print(texto_encontrado)
        dados[f"resultado: {j}"] = texto_encontrado
        j += 1
        #Extrair CPF/CNPJ
        """
        padrao = r'CNPJ:\s*([\d./-]+)'
        new_resultado = re.findall(padrao, texto_encontrado, re.DOTALL)
        print("CPF/CNPJ: ",new_resultado)
        #Extrair Valor global
        padrao = r'Valor:\s*R\$\s*([\d,.]+)'
        new_resultado = re.findall(padrao, texto_encontrado, re.DOTALL)
        print("Valor: ",new_resultado)
        #extrair data
        padrao = r'PB, \b\d{1,2}\s+de\s+([A-Za-zç]+)\s+de\s+\d{4}\b'
        new_resultado = re.search(padrao, texto_encontrado, re.DOTALL)
        print("Data: ", new_resultado.group(0))
        #extrair municipio
        padrao = r"([^\n]+?)\s*-\s*PB"
        new_resultado = re.findall(padrao, texto_encontrado, re.IGNORECASE | re.UNICODE)
        print("Municipio: ", new_resultado)
        """
        #Extrair Codigo
        print("Código Identificador:", codigo_identificador)
