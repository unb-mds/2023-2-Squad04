from collections import defaultdict
from datetime import datetime
import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

def ler_dados_novo_json(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
        dados_json = json.load(arquivo_json)
    return dados_json

def extrair_dados_novo_json(dados_pdf):
    contagem = defaultdict(lambda: defaultdict(int))
    total_todos = defaultdict(int)

    for item in dados_pdf:
        municipio = item["Municipio"]
        pdf_data = item["Data"]

        # Extrair o mês e o ano da data
        mes = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%b")
        ano = datetime.strptime(pdf_data, "%Y-%m-%d").strftime("%Y")

        # Incrementar as contagens corretamente
        contagem[municipio][mes] += 1
        total_todos[mes] += 1

    # Criar a lista de saída com todas as combinações de municípios e meses
    municipios = ["Água Branca","Aguiar","Alagoa Grande","Alagoa Nova","Alagoinha","Alcantil","Algodão de Jandaíra","Alhandra","Amparo","Aparecida","Araçagi","Arara","Araruna","Areia","Areia de Baraúnas","Areial","Aroeiras","Assunção","Baía da Traição","Bananeiras","Baraúna","Barra de Santa Rosa","Barra de Santana","Barra de São Miguel","Bayeux","Belém","Belém do Brejo do Cruz","Bernardino Batista","Boa Ventura","Boa Vista","Bom Jesus","Bom Sucesso","Bonito de Santa Fé","Boqueirão","Borborema","Brejo do Cruz","Brejo dos Santos","Caaporã","Cabaceiras","Cabedelo","Cachoeira dos Índios","Cacimba de Areia","Cacimba de Dentro","Cacimbas","Caiçara","Cajazeiras","Cajazeirinhas","Caldas Brandão","Camalaú","Campina Grande","Capim","Caraúbas","Carrapateira","Casserengue","Catingueira","Catolé do Rocha","Caturité","Conceição","Condado","Conde","Congo","Coremas","Coxixola","Cruz do Espírito Santo","Cubati","Cuité","Cuité de Mamanguape","Cuitegi","Curral de Cima","Curral Velho","Damião","Desterro","Diamante","Dona Inês","Duas Estradas","Emas","Esperança","Fagundes","Frei Martinho","Gado Bravo","Guarabira","Gurinhém","Gurjão","Ibiara","Igaracy","Imaculada","Ingá","Itabaiana","Itaporanga","Itapororoca","Itatuba","Jacaraú","Jericó","João Pessoa","Joca Claudino","Juarez Távora","Juazeirinho","Junco do Seridó","Juripiranga","Juru","Lagoa de Dentro","Lagoa Seca","Lastro","Livramento","Logradouro","Lucena","Mãe d'Água","Malta","Mamanguape","Manaíra","Marcação","Mari","Marizópolis","Massaranduba","Mataraca","Matinhas","Mato Grosso","Maturéia","Mogeiro","Montadas","Monte Horebe","Monteiro","Mulungu","Natuba","Nazarezinho","Nova Floresta","Nova Olinda","Nova Palmeira","Olho d'Água","Olivedos","Ouro Velho","Parari","Passagem","Patos","Paulista","Pedra Branca","Pedra Lavrada","Pedras de Fogo","Pedro Régis","Piancó","Picuí","Pilar","Pilões","Pilõezinhos","Pirpirituba","Pitimbu","Pocinhos","Poço Dantas ","Poço de José de Moura","Pombal","Prata","Princesa Isabel","Puxinanã","Queimadas","Quixabá","Remígio","Riachão","Riachão do Bacamarte","Riachão do Poço","Riacho de Santo Antônio","Riacho dos Cavalos","Rio Tinto","Salgadinho","Salgado de São Félix","Santa Cecília","Santa Cruz","Santa Helena","Santa Inês","Santa Luzia","Santa Rita","Santa Terezinha","Santana de Mangueira","Santana dos Garrotes","Santo André","São Bentinho","São Bento","São Domingos","São Domingos do Cariri","São Francisco","São João do Cariri","São João do Rio do Peixe","São João do Tigre","São José da Lagoa Tapada","São José de Caiana","São José de Espinharas","São José de Piranhas","São José de Princesa","São José do Bonfim","São José do Brejo do Cruz","São José do Sabugi","São José dos Cordeiros","São José dos Ramos","São Mamede","São Miguel de Taipu","São Sebastião de Lagoa de Roça","São Sebastião do Umbuzeiro","São Vicente do Seridó","Sapé","Serra Branca","Serra da Raiz","Serra Grande","Serra Redonda","Serraria","Sertãozinho","Sobrado","Solânea","Soledade","Sossêgo","Sousa","Sumé","Tacima","Taperoá","Tavares","Teixeira","Tenório","Triunfu","Uiraúna","Umbuzeiro","Várzea","Vieirópolis","Vista Serrana","Zabelê","Lagoa"]
    meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    saida_json = []
    for municipio in municipios:
        for mes in meses:
            qtd = contagem[municipio][mes]
            saida_json.append({"municipio": municipio, "mes": mes, "qtd": qtd, "ano": ano})

    return saida_json

dados_pdf_novo_entrada = ler_dados_novo_json(diretorio_atual + "/dados/data.json")
saida_json_novo = extrair_dados_novo_json(dados_pdf_novo_entrada)

with open(diretorio_atual + "/dados/counter.json", "w", encoding="utf-8") as arquivo_saida:
    json.dump(saida_json_novo, arquivo_saida, indent=2, ensure_ascii=False)

print("Arquivo JSON gerado com sucesso.")
