import PyPDF2
import re

# Função para extrair informações relevantes de uma linha
def extract_info(line):
    # Use expressões regulares para extrair os valores
    match = re.search(r'Município: (.*?), Objetivo: (.*?), Data: (.*?), Código: (.*?), Valor: (R\$ [\d.,]+)', line)
    if match:
        return f'Município: {match.group(1)}, Objetivo: {match.group(2)}, Data: {match.group(3)}, Código: {match.group(4)}, Valor: {match.group(5)}'
    return None

# Abra o arquivo PDF
pdf_file = open(r'C:\Users\julii\OneDrive\Documentos\2023-2-Squad04\Code\teste\pdf.csv', 'rb')  # Use um caminho absoluto ou caminho relativo correto

# Crie um objeto PDF Reader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Variável para armazenar as informações relevantes
info = []

# Percorra todas as páginas do PDF
for page in pdf_reader.pages:
    text = page.extract_text()
    lines = text.split('\n')
    
    for line in lines:
        # Verifique se a linha contém informações relevantes
        info_line = extract_info(line)
        if info_line:
            info.append(info_line)

# Feche o arquivo PDF
pdf_file.close()

# Imprima o resultado
for item in info:
    print(item)
