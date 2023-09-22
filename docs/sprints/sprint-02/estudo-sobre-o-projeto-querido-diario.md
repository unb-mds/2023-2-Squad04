<header>
    Sprint 02 - Oceano de Tarefas
</header>
<div class="doc-body">
<!-- ADD O CONTEÚDO ABAIXO -->

# Estudo do Projeto "Querido Diário" da Open Knowledge Brasil

## História
O Querido Diário é resultante de uma junção entre duas ideias semelhantes, a primeira delas se chamava "Projeto Nosso Querido Diário Oficial" e foi concebida pela [Open Knowledge Brasil](https://ok.org.br/). O projeto estabeleceu metodologias para a extração de infomações presentes nos diários oficiais, dividindo a comunidade em dois importantes grupos, os curadores que identificavam informações que seriam de interesse e também os experts, que codificariam os raspadores de dados. 

Já a segunda ideia foi inspirada no sucesso da [Operação Serenata de Amor](https://serenata.ai/), operação que por meio de uma robô chamada Rosie, expôs suspeitas de mal uso de dinheiro público pelos deputados federais.

<iframe src="https://www.facebook.com/plugins/video.php?height=410&href=https%3A%2F%2Fwww.facebook.com%2FoperacaoSerenataDeAmor%2Fvideos%2F555858474606479%2F&show_text=false&width=560&t=0" width="560" height="410" style="border:none;overflow:hidden" scrolling="no" frameborder="0" allowfullscreen="true" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share" allowFullScreen="true"></iframe>

Em 2018, a Open Knowledge Brasil definiu que o código base a ser usado no **Querido Diário**, seria o código do projeto Querido Diário da Serenata.

A iniciativa inicialmente visava coletar diários oficiais municipais e analisar dispensas de licitação, mas enfrentou desafios técnicos e falta de engajamento. No ano seguinte, a comunidade se concentrou em criar raspadores de arquivos para aumentar a cobertura em municípios brasileiros, alcançando mais de 2.200 municípios em menos de dois anos. No segundo semestre de 2020, obtiveram financiamento do projeto Empatía da ILDA, patrocinado pelo Banco Interamericano de Desenvolvimento, permitindo o desenvolvimento de uma API e uma plataforma de busca. A plataforma oficial, chamada Querido Diário, foi lançada em 20 de julho de 2021, permitindo buscas por palavras-chave, municípios e datas.

## Querido Diário na mídia
- [G1 - Projeto brasileiro que dá transparência a publicações oficiais é premiado na Cúpula do Prêmio Nobel](https://g1.globo.com/mundo/noticia/2023/05/25/projeto-brasileiro-que-da-transparencia-a-publicacoes-oficiais-e-premiado-na-cupula-do-premio-nobel.ghtml)
- [Jornal Nacional - Fundação Nobel reúne especialistas para discutir propostas de combate à desinformação](https://g1.globo.com/jornal-nacional/noticia/2023/05/25/fundacao-nobel-reune-especialistas-para-discutir-propostas-de-combate-a-desinformacao.ghtml)
- [Tecnologia fortalece o controle social no 'deserto de dados' sobre os governos](https://drive.google.com/file/d/14dO2j39WJltfzajs4-trm1FS9aMAfCtl/view)
- [Bom Dia Brasil - Tecnologia ajuda cidadãos a fiscalizar o trabalho do poder público - 27/09/2022](https://globoplay.globo.com/v/10969433/)

## Arquitetura e fluxo de dados
![Arquitetura e fluxo de dados](https://queridodiario.ok.org.br/assets/images/arch.png)

## Coleta de dados
A coleta de arquivos de diários oficiais é feita por meio de scripts desenvolvidos com o framework Scrapy, permitindo a raspagem de dados de diferentes municípios. Esses scripts são chamados de "spiders" e estão disponíveis em um repositório para a comunidade.

## Censo
Antes de criar os spiders, é necessário identificar onde os diários oficiais de cada município são publicados na web, o que pode ser um desafio devido à falta de padrão. Para isso, foi criada a iniciativa ["Censo Querido Diário"](https://censo.ok.org.br/), onde qualquer pessoa pode enviar informações sobre a fonte de publicação de diários de um município. Essas informações são validadas por voluntários e usadas para análises sobre a divulgação de atos públicos no Brasil.
- [Repositório](https://github.com/okfn-brasil/censo-querido-diario)

## Processamento de dados
Nesta etapa, os dados coletados são processados para transformá-los em formato aberto e integrados em outras partes do sistema. Ferramentas como [Apache Tika](https://tika.apache.org/) para extração de texto, [Elasticsearch](https://www.elastic.co/) para indexação de documentos e [PostgreSQL](https://www.postgresql.org/) para gerenciamento de dados são usadas. Além disso, Python é amplamente utilizado para essa tarefa.
- [Repositório](https://github.com/okfn-brasil/querido-diario-data-processing/)

## Toolbox e API Pública
O [Querido Diário Toolbox](https://github.com/okfn-brasil/querido-diario-toolbox) oferece um conjunto de ferramentas para análise e manipulação dos dados extraídos dos diários oficiais. Essas ferramentas permitem realizar análises exploratórias, limpeza de dados e extração de informações relevantes, como CPF e CNPJ. O projeto Toolbox é colaborativo e continuamente atualizado pela comunidade.

A [API pública](https://queridodiario.ok.org.br/api/docs) é uma parte fundamental do projeto, tornando os dados acessíveis e automatizáveis para máquinas, além de oferecer acesso direto aos desenvolvedores e pesquisadores. Foi construída em Python com [FastAPI](https://fastapi.tiangolo.com/) e possui documentação automática no [Swagger](https://swagger.io/). Ideias e contribuições para a API são bem-vindas no repositório oficial.
- [repositório](https://github.com/okfn-brasil/querido-diario-api)






<!-- ADD O CONTEÚDO ACIMA -->
</div>