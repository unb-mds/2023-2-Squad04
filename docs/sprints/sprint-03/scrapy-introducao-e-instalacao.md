<header>
    Sprint 03 - Maré de Produtividade
</header>
<div class="doc-body">
<!-- ADD O CONTEÚDO ABAIXO -->

# 📜 Introdução ao Scrapy e tutorias de instalação

## O que é o Scrapy? 🤔
O Scrapy é um framework de web scraping de código aberto em Python usado para extrair informações de sites da web de maneira automatizada. Web scraping é o processo de coletar dados de páginas da web de forma programática, em vez de manualmente, o que é útil para várias finalidades, como coletar dados para análise, pesquisa, mineração de dados, entre outras.

O Scrapy fornece uma estrutura robusta e flexível para desenvolver [spiders](#nossa-primeira-spyder-🕷️), que são programas que navegam na web, fazem solicitações HTTP para páginas da web, extraem dados de interesse e armazenam esses dados em um formato estruturado, como JSON, CSV ou em um banco de dados. Além disso, o Scrapy lida com tarefas como gerenciamento de cookies, tratamento de redirecionamentos, paralelismo de solicitações e muito mais.

**Clique** 👉 [**aqui**](https://github.com/unb-mds/2023-2-Squad04/blob/main/prototipos/tutorial_spyder/) **e tenha acesso ao nosso protótipo**

## Instalação do Scrapy 👨‍🔧 
Para começar a usar o Scrapy, siga estas etapas para a instalação: <br>
**⚠️ Certifique-se de que você tenha o Python instalado em seu sistema. O Scrapy requer Python 3.8+**
1. Verificando a versão do python: `python --version`
2. Instalando o scrapy: 
 - Se você estiver usando Anaconda ou Miniconda, você pode instalar a partir do canal conda-forge, que possui pacotes atualizados para Linux, Windows e macOS: `conda install -c conda-forge scrapy`
 - Como alternativa, se você já estiver familiarizado com a instalação de pacotes Python, você pode instalar o Scrapy e suas dependências do PyPI com: `pip install scrapy`
 - Verifique a instalação: `scrapy --version` <br>
 
 3. ⚠️ **Em caso de erros, crie um Ambiente Virtual (Recomendado para evitar conflitos entre pacotes instalados no sistema):**
 - Primeiro, crie um ambiente virtual: `python3 -m venv meuambiente`
 - Ative o ambiente virtual: `source meuambiente/bin/activate`
 - Instale o scrapy: `pip install scrapy`
 - Para sair do ambiente virtual, basta digitar o seguinte comando: `deactivate`


## Exemplo de utilização do Scrapy 🧐
Vamos raspar [quotes.toscrape.com](quotes.toscrape.com), um site que lista citações de autores famosos.

### Nossa primeira Spyder 🕷️

Spiders são classes que você define e que o Scrapy usa para raspar informações de um site (ou de um grupo de sites).

#### Criando um projeto

Antes de começar a fazer web scraping, você precisará configurar um novo projeto Scrapy. Acesse um diretório onde você deseja armazenar seu código e execute:
`scrapy startproject tutorial`

Isso criará um diretório com o seguinte conteúdo:
```
tutorial/
    scrapy.cfg            # arquivo de configuração para implantação

    tutorial/             # módulo Python do projeto, você importará seu código a partir daqui
        __init__.py

        items.py          # arquivo de definição de itens do projeto

        middlewares.py    # arquivo de middlewares do projeto

        pipelines.py      # arquivo de pipelines do projeto

        settings.py       # arquivo de configurações do projeto

        spiders/          # um diretório onde você colocará suas spiders posteriormente
            __init__.py

```

Este é o código para a nossa primeira Spider.

```python
from pathlib import Path

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
```

Como você pode ver, nossa Spider é uma subclasse de scrapy.Spider e define alguns atributos e métodos:

- **name:** identifica a Spider. Ele deve ser exclusivo dentro de um projeto, ou seja, você não pode definir o mesmo nome para diferentes Spiders.

- **start_requests():** deve retornar um iterável de Requests (você pode retornar uma lista de solicitações ou escrever uma função geradora) a partir das quais a Spider começará a rastrear. Solicitações subsequentes serão geradas sucessivamente a partir dessas solicitações iniciais.

- **parse():** um método que será chamado para lidar com a resposta baixada para cada uma das solicitações feitas. O parâmetro de resposta é uma instância de TextResponse que contém o conteúdo da página e possui métodos adicionais úteis para lidar com ele.

- O método **parse()** geralmente analisa a resposta, extrai os dados raspados como dicionários e também encontra novas URLs para seguir, criando novas solicitações a partir delas.

#### Como executar nossa spyder 💻
Para colocar nossa spider para trabalhar, vá para o diretório de nível superior do projeto e execute:<br>
`scrapy crawl quotes`

Este comando executa a spider com o nome que acabamos de adicionar, que enviará algumas solicitações para o domínio. Você receberá uma saída semelhante a esta:

```
... (omitted for brevity)
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Spider opened
2016-12-16 21:24:05 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2016-12-16 21:24:05 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://quotes.toscrape.com/robots.txt> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/1/> (referer: None)
2016-12-16 21:24:05 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://quotes.toscrape.com/page/2/> (referer: None)
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-1.html
2016-12-16 21:24:05 [quotes] DEBUG: Saved file quotes-2.html
2016-12-16 21:24:05 [scrapy.core.engine] INFO: Closing spider (finished)
...
```

Agora, verifique os arquivos no diretório atual. Você deve notar que dois novos arquivos foram criados: **quotes-1.html** e **quotes-2.html**, com o conteúdo correspondente às respectivas URLs, conforme nosso método instrui.

#### O que aconteceu nos bastidores? 🤔

O Scrapy agendou os objetos retornados pelo método da Spider. Ao receber uma resposta para cada um deles, ele cria objetos de Resposta e chama o método de retorno de chamada associado à solicitação (neste caso, o método "parse"), passando a resposta como argumento.

#### Raspando apenas os dados e salvando em um .json 💾
O código abaixo é um exemplo de uma spider que raspa dados das páginas, em vez de salvar o HTML como fazia a do exemplo anterior.

**Clique** 👉 [**aqui**](https://github.com/unb-mds/2023-2-Squad04/blob/main/prototipos/tutorial_spyder/) **e tenha acesso ao nosso protótipo**

```
import scrapy

class QuotesSpider(scrapy.Spider):
    # Nome do spider
    name = "quotes"

    # URLs iniciais a serem raspadas
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    # Função que é chamada para processar cada página
    def parse(self, response):
        # Loop através de cada elemento 'div.quote' na página
        for quote in response.css("div.quote"):
            # Extrai o texto da citação usando o seletor CSS
            text = quote.css("span.text::text").get()
            # Extrai o autor da citação usando o seletor CSS
            author = quote.css("span small::text").get()
            # Extrai todas as tags da citação usando o seletor CSS
            tags = quote.css("div.tags a.tag::text").getall()

            # Cria um dicionário com os dados extraídos
            quote_data = {
                "text": text,
                "author": author,
                "tags": tags,
            }

            # Retorna o dicionário como resultado do processamento da página
            yield quote_data

        # Verifica se há uma próxima página
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            # Se houver uma próxima página, segue o link e chama 'parse' novamente
            yield response.follow(next_page, self.parse)

```
Você pode armazenar os dados extraídos em um formato de sua escolha, como JSON, CSV ou em um banco de dados. Para salvar os dados em um arquivo JSON, você pode usar o seguinte comando: `scrapy crawl livros -o livros.json`

# 🕵️ Para saber mais...
Esse tutorial se baseou na documentação oficial do scrapy, se você quiser saber mais a fundo sobre todas as funcionalidades disponíveis da ferramenta, clique 👉 [aqui](https://docs.scrapy.org/en/latest/index.html) e acesse a documentação completa.

<!-- ADD O CONTEÚDO ACIMA -->
</div>