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
nome_arquivo = file_path

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
            data = pdf_name.split('_')[2]
            
            #encontra municipio
            municipios = ["Água Branca","Aguiar","Alagoa Grande","Alagoa Nova","Alagoinha","Alcantil","Algodão de Jandaíra","Alhandra","Amparo","Aparecida","Araçagi","Arara","Araruna","Areia de Baraúnas","Areial","Aroeiras","Assunção","Baía da Traição","Bananeiras","Baraúna","Barra de Santa Rosa","Barra de Santana","Barra de São Miguel","Bayeux","Belém do Brejo do Cruz","Bernardino Batista","Boa Ventura","Boa Vista","Bom Jesus","Bom Sucesso","Bonito de Santa Fé","Boqueirão","Borborema","Brejo do Cruz","Brejo dos Santos","Caaporã","Cabaceiras","Cabedelo","Cachoeira dos Índios","Cacimba de Areia","Cacimba de Dentro","Cacimbas","Caiçara","Cajazeiras","Cajazeirinhas","Caldas Brandão","Camalaú","Campina Grande","Capim","Caraúbas","Carrapateira","Casserengue","Catingueira","Catolé do Rocha","Caturité","Conceição","Condado","Conde","Congo","Coremas","Coxixola","Cruz do Espírito Santo","Cubati","Cuité de Mamanguape","Cuitegi","Curral de Cima","Curral Velho","Damião","Desterro","Diamante","Dona Inês","Duas Estradas","Emas","Esperança","Fagundes","Frei Martinho","Gado Bravo","Guarabira","Gurinhém","Gurjão","Ibiara","Igaracy","Imaculada","Ingá","Itabaiana","Itaporanga","Itapororoca","Itatuba","Jacaraú","Jericó","João Pessoa","Joca Claudino","Juarez Távora","Juazeirinho","Junco do Seridó","Juripiranga","Juru","Lagoa de Dentro","Lagoa Seca","Lastro","Livramento","Logradouro","Lucena","Mãe d'Água","Malta","Mamanguape","Manaíra","Marcação","Marizópolis","Mari","Massaranduba","Mataraca","Matinhas","Mato Grosso","Maturéia","Mogeiro","Montadas","Monte Horebe","Mulungu","Natuba","Nazarezinho","Nova Floresta","Nova Olinda","Nova Palmeira","Olho d'Água","Olivedos","Ouro Velho","Parari","Passagem","Patos","Paulista","Pedra Branca","Pedra Lavrada","Pedras de Fogo","Pedro Régis","Piancó","Picuí","Pilar","Pilões","Pilõezinhos","Pirpirituba","Pitimbu","Pocinhos","Poço Dantas ","Poço de José de Moura","Pombal","Prata","Princesa Isabel","Puxinanã","Queimadas","Quixabá","Remígio","Riachão do Bacamarte","Riachão do Poço","Riachão","Riacho de Santo Antônio","Riacho dos Cavalos","Rio Tinto","Salgadinho","Salgado de São Félix","Santa Cecília","Santa Cruz","Santa Helena","Santa Inês","Santa Luzia","Santa Rita","Santa Terezinha","Santana de Mangueira","Santana dos Garrotes","Santo André","São Bentinho","São Bento","São Domingos","São Domingos do Cariri","São Francisco","São João do Cariri","São João do Rio do Peixe","São João do Tigre","São José da Lagoa Tapada","São José de Caiana","São José de Espinharas","São José de Piranhas","São José de Princesa","São José do Bonfim","São José do Brejo do Cruz","São José do Sabugi","São José dos Cordeiros","São José dos Ramos","São Mamede","São Miguel de Taipu","São Sebastião de Lagoa de Roça","São Sebastião do Umbuzeiro","São Vicente do Seridó","Sapé","Serra Branca","Serra da Raiz","Serra Grande","Serra Redonda","Serraria","Sertãozinho","Sobrado","Solânea","Soledade","Sossêgo","Sousa","Sumé","Tacima","Taperoá","Tavares","Teixeira","Tenório","Triunfu","Uiraúna","Umbuzeiro","Várzea","Vieirópolis","Vista Serrana","Zabelê","Lagoa","Belém","Cuité","Areia","Monteiro"]
            municipio = ''
            
            for i in municipios:
                if i.lower() in texto_encontrado.lower():
                    municipio = i
                    break           
            
            #Extrair Codigo
            dados_json = {
                "Titulo_PDF": pdf_name,
                "Texto_encontrado": texto_encontrado,
                "Codigo_identificador": codigo_identificador,
                "Data": data,
                "Municipio": municipio
            }
            
            with open(f'{save_path}/data.json', 'r', encoding="utf-8") as arquivo_json:
                old_json = json.load(arquivo_json)
            
            old_json.append(dados_json)
            
            with open(f'{save_path}/data.json', "w", encoding="utf-8") as arquivo_json:
                json.dump(old_json, arquivo_json, ensure_ascii=False,indent=2) 
