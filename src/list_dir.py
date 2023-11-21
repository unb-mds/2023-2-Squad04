import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def listar_arquivos(diretorio):
    try:
        arquivos = os.listdir(diretorio)

        arquivos = [arquivo for arquivo in arquivos if diretorio_atual]

        return arquivos
    except OSError as e:
        print(f"Erro ao listar arquivos: {e}")
        return None

def salvar(arquivos, caminho_txt):
    try:
        with open(caminho_txt, 'w') as arquivo_txt:
            arquivo_txt.write('\n'.join(arquivos))
        print(f"Lista de arquivos salva em {caminho_txt}")
    except Exception as e:
        print(f"Erro ao salvar em txt: {e}")


caminho_diretorio = diretorio_atual + '/pdfs'

caminho_txt = diretorio_atual + '/lista_pdfs.txt'

arquivos = listar_arquivos(caminho_diretorio)

if arquivos:
    salvar(arquivos, caminho_txt)
