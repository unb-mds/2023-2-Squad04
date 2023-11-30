import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

lista_pdfs = os.path.join(diretorio_atual, 'lista_pdfs.txt')
arquivos = []

with open(lista_pdfs, "r", encoding="utf-8") as arquivo_txt:
    arquivos = arquivo_txt.readlines()

for i in range(len(arquivos)):
    pdf_name = arquivos[i].strip()
    os.remove(diretorio_atual + "/pdfs/" + pdf_name)