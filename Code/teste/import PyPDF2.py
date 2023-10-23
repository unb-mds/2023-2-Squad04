import PyPDF2
import csv
import re

# Função para extrair informações relevantes de uma linha
def extract_info(line):
    # Use expressões regulares para extrair os valores
    match = re.search(r'Município: (.*?), Objetivo: (.*?), Data: (.*?), Código: (.*?), Valor: (R\$ [\d.,]+)', line)
    if match:
        return match.groups()
    return None

# Abra o arquivo PDF
pdf_file = open(r'C:\Users\julii\OneDrive\Documentos\2023-2-Squad04\Code\teste\test.pdf', 'rb')  # Use um caminho absoluto ou caminho relativo correto

# Crie um objeto PDF Reader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Crie um arquivo CSV para escrever os dados
csv_file = open('dados.csv', 'w', newline='', encoding='utf-8')  # Adicione encoding para suportar caracteres especiais
csv_writer = csv.writer(csv_file)

# Variável para acompanhar as informações
info = []

# Percorra todas as páginas do PDF
for page in pdf_reader.pages:
    text = page.extract_text()
    lines = text.split('\n')
    
    for line in lines:
        # Verifique se a linha contém informações relevantes
        if 'Município:' in line:
            info = extract_info(line)
            if info:
                csv_writer.writerow(info)
        else:
            # Se a linha não contém informações relevantes, escreva-a no arquivo CSV
            csv_writer.writerow([line])

# Feche os arquivos
pdf_file.close()
csv_file.close()
