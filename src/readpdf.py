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
            municipios = ["Água Branca – PB","Aguiar – PB","Alagoa Grande – PB","Alagoa Nova – PB","Alagoinha – PB","Alcantil – PB","Algodão de Jandaíra – PB","Alhandra – PB","Amparo – PB","Aparecida – PB","Araçagi – PB","Arara – PB","Araruna – PB","Areia de Baraúnas – PB","Areial – PB","Aroeiras – PB","Assunção – PB","Baía da Traição – PB","Bananeiras – PB","Baraúna – PB","Barra de Santa Rosa – PB","Barra de Santana – PB","Barra de São Miguel – PB","Bayeux – PB","Belém do Brejo do Cruz – PB","Bernardino Batista – PB","Boa Ventura – PB","Boa Vista – PB","Bom Jesus – PB","Bom Sucesso – PB","Bonito de Santa Fé – PB","Boqueirão – PB","Borborema – PB","Brejo do Cruz – PB","Brejo dos Santos – PB","Caaporã – PB","Cabaceiras – PB","Cabedelo – PB","Cachoeira dos Índios – PB","Cacimba de Areia – PB","Cacimba de Dentro – PB","Cacimbas – PB","Caiçara – PB","Cajazeiras – PB","Cajazeirinhas – PB","Caldas Brandão – PB","Camalaú – PB","Campina Grande – PB","Capim – PB","Caraúbas – PB","Carrapateira – PB","Casserengue – PB","Catingueira – PB","Catolé do Rocha – PB","Caturité – PB","Conceição – PB","Condado – PB","Conde – PB","Congo – PB","Coremas – PB","Coxixola – PB","Cruz do Espírito Santo – PB","Cubati – PB","Cuité de Mamanguape – PB","Cuitegi – PB","Curral de Cima – PB","Curral Velho – PB","Damião – PB","Desterro – PB","Diamante – PB","Dona Inês – PB","Duas Estradas – PB","Emas – PB","Esperança – PB","Fagundes – PB","Frei Martinho – PB","Gado Bravo – PB","Guarabira – PB","Gurinhém – PB","Gurjão – PB","Ibiara – PB","Igaracy – PB","Imaculada – PB","Ingá – PB","Itabaiana – PB","Itaporanga – PB","Itapororoca – PB","Itatuba – PB","Jacaraú – PB","Jericó – PB","João Pessoa – PB","Joca Claudino – PB","Juarez Távora – PB","Juazeirinho – PB","Junco do Seridó – PB","Juripiranga – PB","Juru – PB","Lagoa de Dentro – PB","Lagoa Seca – PB","Lastro – PB","Livramento – PB","Logradouro – PB","Lucena – PB","Mãe d'Água – PB","Malta – PB","Mamanguape – PB","Manaíra – PB","Marcação – PB","Marizópolis – PB","Mari – PB","Massaranduba – PB","Mataraca – PB","Matinhas – PB","Mato Grosso – PB","Maturéia – PB","Mogeiro – PB","Montadas – PB","Monte Horebe – PB","Mulungu – PB","Natuba – PB","Nazarezinho – PB","Nova Floresta – PB","Nova Olinda – PB","Nova Palmeira – PB","Olho d'Água – PB","Olivedos – PB","Ouro Velho – PB","Parari – PB","Passagem – PB","Patos – PB","Paulista – PB","Pedra Branca – PB","Pedra Lavrada – PB","Pedras de Fogo – PB","Pedro Régis – PB","Piancó – PB","Picuí – PB","Pilar – PB","Pilões – PB","Pilõezinhos – PB","Pirpirituba – PB","Pitimbu – PB","Pocinhos – PB","Poço Dantas  – PB","Poço de José de Moura – PB","Pombal – PB","Prata – PB","Princesa Isabel – PB","Puxinanã – PB","Queimadas – PB","Quixabá – PB","Remígio – PB","Riachão do Bacamarte – PB","Riachão do Poço – PB","Riachão – PB","Riacho de Santo Antônio – PB","Riacho dos Cavalos – PB","Rio Tinto – PB","Salgadinho – PB","Salgado de São Félix – PB","Santa Cecília – PB","Santa Cruz – PB","Santa Helena – PB","Santa Inês – PB","Santa Luzia – PB","Santa Rita – PB","Santa Terezinha – PB","Santana de Mangueira – PB","Santana dos Garrotes – PB","Santo André – PB","São Bentinho – PB","São Bento – PB","São Domingos – PB","São Domingos do Cariri – PB","São Francisco – PB","São João do Cariri – PB","São João do Rio do Peixe – PB","São João do Tigre – PB","São José da Lagoa Tapada – PB","São José de Caiana – PB","São José de Espinharas – PB","São José de Piranhas – PB","São José de Princesa – PB","São José do Bonfim – PB","São José do Brejo do Cruz – PB","São José do Sabugi – PB","São José dos Cordeiros – PB","São José dos Ramos – PB","São Mamede – PB","São Miguel de Taipu – PB","São Sebastião de Lagoa de Roça – PB","São Sebastião do Umbuzeiro – PB","São Vicente do Seridó – PB","Sapé – PB","Serra Branca – PB","Serra da Raiz – PB","Serra Grande – PB","Serra Redonda – PB","Serraria – PB","Sertãozinho – PB","Sobrado – PB","Solânea – PB","Soledade – PB","Sossêgo – PB","Sousa – PB","Sumé – PB","Tacima – PB","Taperoá – PB","Tavares – PB","Teixeira – PB","Tenório – PB","Triunfu – PB","Uiraúna – PB","Umbuzeiro – PB","Várzea – PB","Vieirópolis – PB","Vista Serrana – PB","Zabelê – PB","Lagoa – PB","Belém – PB","Cuité – PB","Areia – PB","Monteiro – PB", "Água Branca - PB","Aguiar - PB","Alagoa Grande - PB","Alagoa Nova - PB","Alagoinha - PB","Alcantil - PB","Algodão de Jandaíra - PB","Alhandra - PB","Amparo - PB","Aparecida - PB","Araçagi - PB","Arara - PB","Araruna - PB","Areia de Baraúnas - PB","Areial - PB","Aroeiras - PB","Assunção - PB","Baía da Traição - PB","Bananeiras - PB","Baraúna - PB","Barra de Santa Rosa - PB","Barra de Santana - PB","Barra de São Miguel - PB","Bayeux - PB","Belém do Brejo do Cruz - PB","Bernardino Batista - PB","Boa Ventura - PB","Boa Vista - PB","Bom Jesus - PB","Bom Sucesso - PB","Bonito de Santa Fé - PB","Boqueirão - PB","Borborema - PB","Brejo do Cruz - PB","Brejo dos Santos - PB","Caaporã - PB","Cabaceiras - PB","Cabedelo - PB","Cachoeira dos Índios - PB","Cacimba de Areia - PB","Cacimba de Dentro - PB","Cacimbas - PB","Caiçara - PB","Cajazeiras - PB","Cajazeirinhas - PB","Caldas Brandão - PB","Camalaú - PB","Campina Grande - PB","Capim - PB","Caraúbas - PB","Carrapateira - PB","Casserengue - PB","Catingueira - PB","Catolé do Rocha - PB","Caturité - PB","Conceição - PB","Condado - PB","Conde - PB","Congo - PB","Coremas - PB","Coxixola - PB","Cruz do Espírito Santo - PB","Cubati - PB","Cuité de Mamanguape - PB","Cuitegi - PB","Curral de Cima - PB","Curral Velho - PB","Damião - PB","Desterro - PB","Diamante - PB","Dona Inês - PB","Duas Estradas - PB","Emas - PB","Esperança - PB","Fagundes - PB","Frei Martinho - PB","Gado Bravo - PB","Guarabira - PB","Gurinhém - PB","Gurjão - PB","Ibiara - PB","Igaracy - PB","Imaculada - PB","Ingá - PB","Itabaiana - PB","Itaporanga - PB","Itapororoca - PB","Itatuba - PB","Jacaraú - PB","Jericó - PB","João Pessoa - PB","Joca Claudino - PB","Juarez Távora - PB","Juazeirinho - PB","Junco do Seridó - PB","Juripiranga - PB","Juru - PB","Lagoa de Dentro - PB","Lagoa Seca - PB","Lastro - PB","Livramento - PB","Logradouro - PB","Lucena - PB","Mãe d'Água - PB","Malta - PB","Mamanguape - PB","Manaíra - PB","Marcação - PB","Marizópolis - PB","Mari - PB","Massaranduba - PB","Mataraca - PB","Matinhas - PB","Mato Grosso - PB","Maturéia - PB","Mogeiro - PB","Montadas - PB","Monte Horebe - PB","Mulungu - PB","Natuba - PB","Nazarezinho - PB","Nova Floresta - PB","Nova Olinda - PB","Nova Palmeira - PB","Olho d'Água - PB","Olivedos - PB","Ouro Velho - PB","Parari - PB","Passagem - PB","Patos - PB","Paulista - PB","Pedra Branca - PB","Pedra Lavrada - PB","Pedras de Fogo - PB","Pedro Régis - PB","Piancó - PB","Picuí - PB","Pilar - PB","Pilões - PB","Pilõezinhos - PB","Pirpirituba - PB","Pitimbu - PB","Pocinhos - PB","Poço Dantas  - PB","Poço de José de Moura - PB","Pombal - PB","Prata - PB","Princesa Isabel - PB","Puxinanã - PB","Queimadas - PB","Quixabá - PB","Remígio - PB","Riachão do Bacamarte - PB","Riachão do Poço - PB","Riachão - PB","Riacho de Santo Antônio - PB","Riacho dos Cavalos - PB","Rio Tinto - PB","Salgadinho - PB","Salgado de São Félix - PB","Santa Cecília - PB","Santa Cruz - PB","Santa Helena - PB","Santa Inês - PB","Santa Luzia - PB","Santa Rita - PB","Santa Terezinha - PB","Santana de Mangueira - PB","Santana dos Garrotes - PB","Santo André - PB","São Bentinho - PB","São Bento - PB","São Domingos - PB","São Domingos do Cariri - PB","São Francisco - PB","São João do Cariri - PB","São João do Rio do Peixe - PB","São João do Tigre - PB","São José da Lagoa Tapada - PB","São José de Caiana - PB","São José de Espinharas - PB","São José de Piranhas - PB","São José de Princesa - PB","São José do Bonfim - PB","São José do Brejo do Cruz - PB","São José do Sabugi - PB","São José dos Cordeiros - PB","São José dos Ramos - PB","São Mamede - PB","São Miguel de Taipu - PB","São Sebastião de Lagoa de Roça - PB","São Sebastião do Umbuzeiro - PB","São Vicente do Seridó - PB","Sapé - PB","Serra Branca - PB","Serra da Raiz - PB","Serra Grande - PB","Serra Redonda - PB","Serraria - PB","Sertãozinho - PB","Sobrado - PB","Solânea - PB","Soledade - PB","Sossêgo - PB","Sousa - PB","Sumé - PB","Tacima - PB","Taperoá - PB","Tavares - PB","Teixeira - PB","Tenório - PB","Triunfu - PB","Uiraúna - PB","Umbuzeiro - PB","Várzea - PB","Vieirópolis - PB","Vista Serrana - PB","Zabelê - PB","Lagoa - PB","Belém - PB","Cuité - PB","Areia - PB","Monteiro - PB"]
            municipio = ''
            
            for i in municipios:
                if i.lower() in texto_encontrado.lower():
                    municipio = i
                    break           
            
            if municipio:
                municipio = municipio.replace(" - PB", "").replace(" – PB", "")

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
