FROM nginx

COPY ./ /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

# Com o terminal na pasta documentation:
# Construa a imagem Docker: docker build -t meu-servidor-web .
# Inicie o contêiner Docker: docker run -d -p 8080:80 -v ./:/usr/share/nginx/html meu-servidor-web
# Acesse em um navegador digitando http://localhost:8080 

# Use o comando "docker ps" para listar os contêineres em execução e "docker stop nome_do_contêiner" para parar o contêiner

