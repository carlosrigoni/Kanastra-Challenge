# Kanastra Challenge

## Setup

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Unix/Mac: `source venv/bin/activate`
   - Windows: `.\venv\Scripts\activate`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute a aplicação: `uvicorn app.main:app --reload`

## Teste de integração
1. Execute `curl -X POST -F "file=@input.csv" http://localhost:8000/api/v1/upload_file` ou `curl -X POST -F "file=@min-input.csv" http://localhost:8000/api/v1/upload_file` com o backend ligado

você pode habilitar logs no arquivo main.py comentando a linha
`logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')`
mas isso afetará tremendamente o desempenho da aplicação, uma maneira de ter os logs e não afetar o desempenho seria telos eles de forma assíncrona com alguma ferramenta externa por exemplo.

## Docker

1. Construa a imagem Docker: `docker-compose build`
2. Inicie o contêiner: `docker-compose up`

## Testes

Execute os testes com: `pytest`
