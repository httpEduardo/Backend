# Golden Raspberry Awards API

## 📖 **Descrição**
A Golden Raspberry Awards API é um serviço RESTful que processa e exibe informações relacionadas ao prêmio **"Pior Filme"** do Golden Raspberry Awards.  
A API permite consultas sobre:
- Filmes vencedores.
- Anos com múltiplos vencedores.
- Intervalos entre vitórias de produtores.

---

##  **Requisitos**
- **Python**: Versão 3.8 ou superior.
- **pip**: Gerenciador de pacotes do Python.
- **Postman** (ou similar): Para testar os endpoints da API.

---

##  **Configuração do Projeto**

### **1. Clonar o Repositório**
Clone o repositório do projeto:
```
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_PROJETO>

2. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para o projeto:


python -m venv venv

Ative o ambiente virtual:

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

3. Instalar Dependências

Instale as dependências do projeto:


pip install -r requirements.txt

4. Configurar o Banco de Dados

A API utiliza um banco de dados SQLite em memória. Os dados do banco são inicializados a partir do arquivo Movielist.csv.

Certifique-se de que o arquivo Movielist.csv está na raiz do projeto.

Executar a API

Inicie o servidor:


python app.py
A API estará disponível no endereço:


http://127.0.0.1:5000
📡 Endpoints da API

1. Buscar Filmes por Ano

Descrição: Retorna todos os filmes de um ano específico.
Método: GET
URL: /api/movies/<ano>
Exemplo:


GET http://127.0.0.1:5000/api/movies/1980
Resposta:


[
  {
    "id": 1,
    "year": 1980,
    "title": "Can't Stop the Music",
    "studios": "Associated Film Distribution",
    "producers": "Allan Carr",
    "winner": true
  }
]

2. Listar Filmes Vencedores

Descrição: Retorna todos os filmes que ganharam o prêmio.
Método: GET
URL: /api/movies/winners
Exemplo:


GET http://127.0.0.1:5000/api/movies/winners
Resposta:


[
  {
    "id": 1,
    "year": 1980,
    "title": "Can't Stop the Music",
    "studios": "Associated Film Distribution",
    "producers": "Allan Carr",
    "winner": true
  }
]

3. Anos com Múltiplos Vencedores

Descrição: Retorna os anos que tiveram mais de um vencedor.
Método: GET
URL: /api/movies/multiple-winners
Exemplo:


GET http://127.0.0.1:5000/api/movies/multiple-winners
Resposta:

[
  {
    "year": 1986,
    "win_count": 2
  }
]

4. Intervalos de Prêmios dos Produtores
Descrição: Retorna o produtor com o maior e menor intervalo entre prêmios consecutivos.
Método: GET
URL: /api/movies/intervals

Exemplo:


GET http://127.0.0.1:5000/api/movies/intervals

Resposta:


{
  "maximum": {
    "producer": "Matthew Vaughn",
    "interval": 13,
    "first_year": 2002,
    "last_year": 2015
  },
  "minimum": {
    "producer": "Joel Silver",
    "interval": 1,
    "first_year": 1990,
    "last_year": 1991
  }
}

5. Tratamento de Erros

Descrição: Retorna uma mensagem amigável para rotas inválidas.
Método: GET
URL: /api/invalid-route
Exemplo:


GET http://127.0.0.1:5000/api/invalid-route
Resposta:


{
  "error": "Rota não encontrada"
}

Testes
Para garantir o funcionamento, a API possui testes de integração utilizando pytest.

Executar os Testes

Certifique-se de que o ambiente virtual está ativo e execute:

pytest

Resultado Esperado


============================= test session starts ==============================
collected 5 items

test_app.py .....                                                      [100%]

============================== 5 passed in 0.45s ===============================

💡 Considerações
Esta API segue o nível 2 do Modelo de Maturidade de Richardson, utilizando métodos HTTP adequados e retornando dados organizados por recursos.