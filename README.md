# Applicação de rota de viagem mais curta

## Considerações
A aplicação em questão foi desenvolvida em Python por se tratar de um teste e ter sido desenvolvido em pouco tempo.

## Docker
Já que a aplicação foi dockerizada, inicie o processo obtendo o Docker Image produzido:

```docker pull ettoreaquino/rota-viagem```

Uma vez carregada a imagem inicie a aplicação executando:

```docker container run -it -p 5000:5000 -e FLASK_APP=src/app.app --rm --name rota-viagem -e FLASK_DEBUG=1 -v $PWD:/app ettoreaquino/rota-viagem```


