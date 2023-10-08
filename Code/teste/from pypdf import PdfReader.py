#pip install PyPDF2
import csv
from PyPDF2 import PdfReader

# Abra o arquivo PDF
reader = PdfReader("test.pdf")

# Crie um novo arquivo CSV de saída
csv_filename = "output.csv"

with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Itere sobre todas as páginas e extraia o texto
    for page in reader.pages:
        text = page.extract_text()
        
        # Escreva o texto no arquivo CSV como uma única coluna
        csv_writer.writerow([text])

