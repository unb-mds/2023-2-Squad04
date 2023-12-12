
<!-- ADD O CONTEÚDO ABAIXO -->
![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/unb-mds/2023-2-Squad04?style=for-the-badge)

# Licitaíba - Extrator de Licitações do Diário Oficial da Paraíba

<p align="center">
<img src="assets/imgs/logo-licitaiba.png" alt="Logo Licitaíba" width="300" style="display: block; margin: 0 auto;">
  <br>
  Logo do projeto Licitaíba
</p>

O projeto "Licitaíba" é uma iniciativa destinada a automatizar a coleta e o acompanhamento de informações relacionadas a licitações públicas no estado da Paraíba, Brasil.

<p align="center">
  <img src="https://www.estudopratico.com.br/wp-content/uploads/2018/06/bandeira-paraiba-1200x675.jpg" alt="Bandeira da Paraíba" width="300" style="display: block; margin: 0 auto;">
  <br>
  Bandeira da Paraíba
</p>

---

## 👨‍🔧 Tutorial para executar o Projeto "Licitaíba"
Este é um guia passo a passo para ajudar você a executar o projeto em sua máquina. Primeiramente você precisa entender como o projeto funciona. Cada script é rodado por agendamento de forma **automática** de segunda a sexta, seguindo uma ordem que deve ser respeitada, tudo isso ocorre pelo git actions.


- [Repositório front-end](https://github.com/unb-mds/2023.2_Licitaiba)
- [Documentação](https://unb-mds.github.io/2023-2-Squad04/#/./)
- [Post mortem](https://unb-mds.github.io/2023-2-Squad04/#/postmortem/postmortem)

### ⚠️ Pré-requisitos
- [Python v3.10.12 ou superior](https://www.python.org/downloads/)


### 1. ⏬ Clonar o Repositório
Para começar, abra o terminal e clone o repositório do GitHub em um diretório local da seguinte maneira:
```
git clone https://github.com/unb-mds/2023-2-Squad04.git
```

### 2. 🚢 Navegar até a pasta "src" 🗂️
Vamos entrar na pasta "src" do projeto usando o terminal. Certifique-se de estar na raiz do repositório clonado:
```
cd 2023-2-Squad04/src
```

### 3. 💻 Baixar pdfs de acordo com a última data resgistrada no pdf_downloader_last_date.txt
Nesse passo, o script de download sempre começa após a data posterior registrada no arquivo txt, ao concluir os downloads, o conteúdo do arquivo é atualizado com a data do último PDF baixado. O script está agendado para rodar às 08:00h., usando o seguinte comando:
```
python3 pdf_downloader.py
```

### 4. 📑 Listar o diretório src/pdfs/ e gravar em um txt todos os pdfs baixados
Essa é a segunda ação programada no repositório que ira ocorrer às 08:10hrs, usando o seguinte comando: 
```
python3 list_dir.py
```

### 5. 📖 Extração das licitações dos pdfs baixados no passo anterior
Seguindo a ordem, essa é a terceira ação programada que ocorrerá às 08:20hrs, usando o seguinte comando: 
```
python3 readpdf.py
```

### 6. 🌐 Contar a quantidade de licitações em cada municipio em todo os dados extraídos no arquivo json gerado pelo readpdf
Quarta ação programada que ocorrerá às 08:30hrs, usando o seguinte comando: 
```
python3 counter.py
```

### 7. 🗑️ Remoção dos Pdfs baixados
Quinto e último comando programado no repositório, que será acionado às 18:30hrs, usando o seguinte comando: 
```
python3 remove_pdf.py
```
<p align="center">
  <img src="assets/imgs/img_home.png"  width="1000" style="display: block; margin: 0 auto;">
</p>
<p align="center">
  <img src="assets/imgs/img_equipeClara.png"  width="1000" style="display: block; margin: 0 auto;">
</p> 
<p align="center">
  <img src="assets/imgs/img_sobre.png" alt="Bandeira da Paraíba" width="1000" style="display: block; margin: 0 auto;">
</p> 
<p align="center">
  <img src="assets/imgs/transicaoEscuroClaro.gif" alt="Bandeira da Paraíba" width="1000" style="display: block; margin: 0 auto;">
</p> 
---

# Integrantes

| Foto| Nome  | Matrícula | Github | 
| ------ | --------- | ------- |----|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/133259317?v=4" alt="carlos">|Carlos Eduardo | 221031265 | [Carlos-kadu](https://github.com/Carlos-kadu)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/42286412?v=4" alt="danilo">|Danilo César|221031149|[DaniloCTM](https://github.com/DaniloCTM)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/117610576?v=4" alt="fernando">|Fernando Gabriel| 221008033|[show-dawn](https://github.com/show-dawn)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/108846009?v=4" alt="julio">|Júlio César| 221007591|[Julio1099](https://github.com/Julio1099)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/94008339?v=4" alt="patricia">|Patrícia Helena|221037993|[patyhelenaa](https://github.com/patyhelenaa)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/85962730?v=4" alt="rayene">|Rayene Ferreira|221022720|[rayenealmeida](https://github.com/rayenealmeida)|
|<img class="pic-squad04" src="https://avatars.githubusercontent.com/u/91281623?v=4" alt="victor">|Victor Moreira|221008481|[aqela-batata-alt](https://github.com/aqela-batata-alt)|

# Papéis da equipe
|Nome|Papel|
|-----|-----|
|Scrum Master| Júlio|
|Arquitetos| Danilo e Victor|
|Product Owner|Carlos|
|Desenvolvedores|Fernando, Rayene e Patrícia|

<!-- ADD O CONTEÚDO ACIMA -->
</div>
