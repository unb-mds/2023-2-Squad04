![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/unb-mds/2023-2-Squad04?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/unb-mds/2023-2-Squad04?style=for-the-badge)

# Licitaíba - Extrator de Licitações do Diário Oficial da Paraíba

<p align="center">
<img src="docs/assets/imgs/logo-licitaiba.png" alt="Logo Licitaíba" width="300" style="display: block; margin: 0 auto;">
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


- Você pode conferir também nosso repositório exclusivo do Front-End -> https://github.com/unb-mds/2023.2_Licitaiba
- Documentação -> https://unb-mds.github.io/2023-2-Squad04/#/./
- Post Mortem -> https://unb-mds.github.io/2023-2-Squad04/#/postmortem/postmortem

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
Portanto, os dados são atualizados e disponibilizados no site https://unb-mds.github.io/2023.2_Licitaiba/ todos os dias às 08:30hrs. 
---


## 🤝 Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Carlos-kadu">
        <img src="https://avatars.githubusercontent.com/u/133259317?v=4" width="100px;" height="100px;" alt="Carlos"/><br>
        <sub>
          <b>Carlos-kadu</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/DaniloCTM">
        <img src="https://avatars.githubusercontent.com/u/42286412?v=4" width="100px;" height="100px;" alt="Danilo"/><br>
        <sub>
          <b>DaniloCTM</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/show-dawn">
        <img src="https://avatars.githubusercontent.com/u/117610576?v=4" width="100px;" height="100px;" alt="Fernando"/><br>
        <sub>
          <b>show-dawn</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/Julio1099">
        <img src="https://avatars.githubusercontent.com/u/108846009?v=4" width="100px;" height="100px;" alt="Júlio"/><br>
        <sub>
          <b>Julio1099</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/patyhelenaa">
        <img src="https://avatars.githubusercontent.com/u/94008339?v=4" width="100px;" height="100px;" alt="Patrícia"/><br>
        <sub>
          <b>patyhelenaa</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/rayenealmeida">
        <img src="https://avatars.githubusercontent.com/u/85962730?v=4" width="100px;" height="100px;" alt="Rayene"/><br>
        <sub>
          <b>rayenealmeida</b>
        </sub>
      </a>
    </td>
     <td align="center">
      <a href="https://github.com/aqela-batata-alt">
        <img src="https://avatars.githubusercontent.com/u/91281623?v=4" width="100px;" height="100px;" alt="Victor"/><br>
        <sub>
          <b>aqela-batata-alt</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📝 Licença 

The [MIT License](https://github.com/AndersonD-art/tasksmobx/commit/64a80024d73a84de3b5a21dfe15dad5fd4c10c7c) (MIT)
