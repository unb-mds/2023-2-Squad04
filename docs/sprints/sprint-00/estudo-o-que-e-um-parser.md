<header>
    Sprint 00 - Procurando Nemo
</header>
<div class="doc-body">
<!-- ADD O CONTEÚDO ABAIXO -->

## Definição e funções

Um parser é um componente de software utilizado para analisar a estrutura de um dado texto ou código fonte. Os parsers são comumente usados em linguagens de programação, compiladores, interpretadores, processamento de linguagem natural (NLP) e em várias outras áreas da computação.

A principal função de um parser é transformar um texto em uma representação estruturada que possa ser facilmente manipulada ou interpretada por um programa. Existem dois tipos principais de parsers:

Parser de Sintaxe (ou Analisador Sintático): Este tipo de parser analisa a estrutura gramatical de um texto para determinar se ele segue as regras da linguagem. Se o texto estiver correto de acordo com a gramática, o parser cria uma árvore de sintaxe ou outra estrutura de dados que representa a estrutura do texto. Caso contrário, ele relata um erro de sintaxe.

Parser de Linguagem de Marcação: Este tipo de parser é usado para analisar linguagens de marcação, como HTML, XML e JSON. Ele identifica os elementos e suas hierarquias no documento, tornando mais fácil a extração de informações ou a manipulação do conteúdo.

Resumindo, um parser desempenha um papel importante na interpretação e manipulação de texto estruturado, tornando-o acessível para processamento por programas de computador. Ele é essencial em muitos domínios da computação e da ciência da computação, desde a análise de código fonte até a análise de documentos e comunicação em redes.

Referências: <br>
https://www.techtarget.com/searchapparchitecture/definition/parser <br>
https://time.cumbuca.com/parsers-n%C3%A3o-tenha-medo-deles-ee104cb27e05 <br>
https://johnidm.gitbooks.io/compiladores-para-humanos/content/part1/syntax-analysis.html <br>
https://www.ic.unicamp.br/~celio/inf533/docs/markup.html <br>

Alguns tutoriais:<br>
https://youtu.be/xYQt8fyXSp0?si=Z1qJkt7FWgb1o3nK <br>
https://youtu.be/CZcU40CcWf8?si=CyVs0P4PWrIKR-8Q <br>


Aqui está um exemplo de um código Python usando parser
```python
import csv

# Nome do arquivo CSV
arquivo_csv = 'dados.csv'

# Função para fazer o parsing do arquivo CSV
def parse_csv(arquivo):
    with open(arquivo, 'r', newline='') as csv_file:
        leitor_csv = csv.DictReader(csv_file)
        
        for linha in leitor_csv:
            nome = linha['Nome']
            idade = int(linha['Idade'])
            profissao = linha['Profissão']
            
            print(f'Nome: {nome}, Idade: {idade}, Profissão: {profissao}')

if __name__ == "__main__":
    parse_csv(arquivo_csv)




