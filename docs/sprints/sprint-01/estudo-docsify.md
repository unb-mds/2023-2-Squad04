<header>
    Sprint 01 - Procurando Dory
</header>
<div class="doc-body">
<!-- ADD O CONTEÚDO ABAIXO -->

## Funcionalidades

1. **Renderização de Markdown**: O Docsify converte arquivos Markdown em páginas HTML interativas e bem formatadas. Isso facilita a criação de conteúdo de documentação sem a necessidade de escrever HTML complexo.

2. **Navegação dinâmica**: O Docsify gera automaticamente uma barra lateral de navegação com base na estrutura de diretórios e arquivos Markdown. Isso simplifica a organização e a navegação na documentação.

3. **Pesquisa em Tempo Real**: O Docsify oferece uma função de pesquisa em tempo real que permite aos usuários encontrar rapidamente o conteúdo relevante na documentação.

4. **Suporte a Plugins**: O Docsify é extensível por meio de plugins, que permitem adicionar funcionalidades extras à documentação, como incorporação de vídeos, integração com métricas de uso, entre outros.

5. **Integração com Vue.js**: O Docsify é construído com base no Vue.js, um framework JavaScript.


# Benefícios

1. **Facilidade de Uso**: O Docsify é simples de configurar e usar. 

2. **Melhor Comunicação**: A documentação é clara e interativa.

3. **Manutenção Simples**: Como a documentação é escrita em Markdown, a manutenção e a atualização são simples. 

4. **Pesquisa Eficaz**: A função de pesquisa em tempo real torna a documentação facilmente pesquisável, economizando tempo para os usuários que procuram informações específicas.


# Instruções de Instalação

1. **Certifique-se de ter o Node.js e o npm instalados**: [nodejs.org](https://nodejs.org/).

2. **Crie um diretório** 
  `mkdir meu-projeto-de-documentacao`
   `cd meu-projeto-de-documentacao`

3. **Inicialize seu projeto Node.js**
    `npm init -y`

4. **Instale o Docsify globalmente**
   `npm install -g docsify-cli`

5. **Crie um diretório para seus arquivos de documentação e adicione um arquivo index.html**
    `mkdir docs`
     `cd docs`
     `touch index.html`


# Uso Básico

1. **Dentro do arquivo index.html escreva o código**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Minha Documentação</title>
</head>
<body>
  <h1>Bem-vindo à Minha Documentação</h1>
  <div id="app"></div>
  <script>
    window.$docsify = {
      name: 'Minha Documentação',
      repo: '',
      loadSidebar: true,
      subMaxLevel: 2
    }
  </script>
  <script src="https://cdn.jsdelivr.net/npm/docsify@latest/dist/docsify.min.js"></script>
</body>
</html>


2. **Volte para o diretório raiz**
    `cd ..`

3. **Inicie um servidor de desenvolvimento Docsify**
    `docsify serve docs`


<!-- ADD O CONTEÚDO ACIMA -->
</div>
