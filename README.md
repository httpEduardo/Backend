# Backend Golden Raspberry Awards

Este projeto é o backend da aplicação **Golden Raspberry Awards**, desenvolvido utilizando **Node.js** e **Express.js**. Ele foi projetado para fornecer uma API REST que gerencia os dados relacionados ao prêmio, permitindo:
- Consultar anos com múltiplos vencedores.
- Listar estúdios com maior número de vitórias.
- Obter produtores com maiores e menores intervalos entre vitórias.
- Consultar filmes vencedores por ano.

---

## **Configuração do Projeto**

### **Pré-requisitos**
Antes de configurar o projeto, certifique-se de que você tenha os seguintes requisitos instalados em sua máquina:
- **Node.js** (versão 16 ou superior)
- **npm** (ou **yarn**, caso prefira)
- Um editor de código, como **Visual Studio Code**

---

### **Instalação**

1. **Clone o Repositório**  
   Faça o clone do repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-repositorio.git
2. **Acesse o Diretório do Projeto**
   Entre na pasta do projeto:
   ```bash
   cd golden-raspberry-backend
3. Instale as Dependências
   Instale todas as dependências necessárias:
   ```bash
   npm install

**Como Executar o Projeto**
Configure o Ambiente
Crie um arquivo .env na raiz do projeto e configure as variáveis de ambiente necessárias. Exemplo:

PORT=3000

Inicie o Servidor
Execute o comando para iniciar o servidor:

npm start
O servidor estará disponível em http://localhost:3000

Endpoints da API
1. Listar Anos com Múltiplos Vencedores
GET /api/years-multiple-winners
Descrição: Retorna os anos em que houve múltiplos vencedores.
Exemplo de Resposta:

[
  { "year": 1986, "winCount": 2 },
  { "year": 1990, "winCount": 2 }
]

. Listar Estúdios com Mais Vitórias
GET /api/top-studios
Descrição: Retorna os estúdios com o maior número de prêmios.
Exemplo de Resposta:
[
  { "studio": "Columbia Pictures", "winCount": 6 },
  { "studio": "Paramount Pictures", "winCount": 6 }
]

Consultar Produtores com Intervalos Entre Vitórias
GET /api/producers-intervals
Descrição: Retorna os produtores com os maiores e menores intervalos entre vitórias.
{
  "max": { "producer": "Matthew Vaughn", "interval": 13 },
  "min": { "producer": "Joel Silver", "interval": 1 }
}

**Consultar Filmes por Ano**
GET /api/movies/:year
Parâmetro: year (ano a ser consultado)
Descrição: Retorna os filmes vencedores do ano especificado.
Exemplo de Resposta:
[
  { "id": 1, "title": "Can't Stop the Music" },
  { "id": 2, "title": "Mommy Dearest" }
]

**Estrutura do Projeto**
O projeto está organizado da seguinte forma:

src/routes: Contém as definições das rotas da API.
src/controllers: Contém a lógica de negócios para cada endpoint.
src/services: Implementa a lógica de manipulação de dados.
src/models: Contém os modelos de dados utilizados no projeto.

