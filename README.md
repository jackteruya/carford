Para ambiente linux.

Com do docker instaldo, caso não tenha -> https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/

Para rodar a aplicação, no docker-compose.yml para subir um container.

    $ docker-compose up



Ou caso não tenha o docker instalado, mas será necessario ter o python instaldo, de preferencia a versão 3.10:
    
    1-Craindo o ambiente:
        $ python -m venv .venv

    2-Ativando o ambiente no linux:
        $ source .venv/bin/activate

    3-Instalando os requisitos:
        $ pip install -r requierements.txt

    4-para rodar o projeto, na raiz do projeto:
        $ python -m main


Endpoint:
 - http://0.0.0.0:8000/api/v1/car/
    - Criar novo car, mas é necessario ter o owner criado, para passar o owner id;
    - existe apenas 3 tipos de cor nessa aplicação `blue`, `yellow` e `gray`;
    - existe apenas 3 tipos de modelos nessa aplicação `convertible`, `hatch` e `sedan`;
    - ex: `curl -X 'POST' \
          'http://0.0.0.0:8000/api/v1/car/' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "name": "string",
          "color": "gray",
          "model": "convertible",
          "owner_id": 26
          }'`
    - ex response: `{
                         "id": 32,
                         "name": "string",
                         "color": "gray",
                         "model": "convertible",
                         "owner": {
                           "id": 26,
                           "name": "string",
                           "date_of_birth": "2023-02-14"
                         }
                       }`
 

 - http://0.0.0.0:8000/api/v1/car/{id}
    - é nessario apenas passar o id do car na url
    - ex: `curl -X 'GET' \
      'http://0.0.0.0:8000/api/v1/car/32/'`
    - ex response: `{
                        "id": 32,
                        "name": "string",
                        "color": "gray",
                        "model": "convertible",
                        "owner": {
                          "id": 26,
                          "name": "string",
                          "date_of_birth": "2023-02-14"
                        }
                      }`
 
 
- http://0.0.0.0:8000/api/v1/car/{id}
    - é nessario apenas passar o id do car na url e retornara a lista dos car do owner
    - ex: `curl -X 'GET' \
      'http://0.0.0.0:8000/api/v1/car/owner/26/'`
    - ex response: `[
                         {
                           "id": 31,
                           "name": "string",
                           "color": "blue",
                           "model": "hatch",
                           "owner": {
                             "id": 26,
                             "name": "string",
                             "date_of_birth": "2023-02-14"
                           }
                         },
                         {
                           "id": 32,
                           "name": "string",
                           "color": "gray",
                           "model": "convertible",
                           "owner": {
                             "id": 26,
                             "name": "string",
                             "date_of_birth": "2023-02-14"
                           }
                         }
                       ]`


 - http://0.0.0.0:8000/api/v1/owner/
    - criar owner
    - ex: `curl -X 'POST' \
        'http://0.0.0.0:8000/api/v1/owner/' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{
        "name": "test",
        "document": "12345678900",
        "date_of_birth": "2000-02-14"
        }'`
    - ex response: `{
                          "id": 27,
                          "name": "test",
                          "document": "12345678900",
                          "date_of_birth": "2000-02-14"
                        }`

 - http://0.0.0.0:8000/api/v1/owner/{id}
    - consulta owner passando o id;
    - ex: `curl -X 'GET' \
          'http://0.0.0.0:8000/api/v1/owner/27' \
           -H 'accept: application/json'`
    - ex response: `{
                      "id": 27,
                        "name": "test",
                        "document": "12345678900",
                        "date_of_birth": "2000-02-14"
                      }`