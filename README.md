# Backend Avançado Pokémon

## 🐱‍🏍 Descrição

Este é o módulo **API principal** de um sistema inspirado no universo Pokémon. Ele serve para gerenciar dados de Pokémons, habilidades e trainers, fornecendo endpoints REST para CRUD, além de consumir APIs externas ou microsserviços conforme necessário. Desenvolvido em Python com FastAPI/Flask (ou outro framework que você usou), com persistência em banco de dados.  

---

## 📦 Funcionalidades Principais

- Listar, criar, atualizar e deletar Pokémons (`GET`, `POST`, `PUT`, `DELETE`)
- Gerenciar habilidades (abilities) e Trainers
- Conectar-se a serviços externos (ex: API pública Pokémon para dados adicionais)
- Testes de rotas principais
- Documentação automática via OpenAPI/Swagger pelo ```bash http://127.0.0.1:5000/openapi

---

## 💻 Tecnologias

- Python  
- FastAPI (ou Flask, dependendo do que você usou)  
- SQLite / MySQL / PostgreSQL (dependendo de sua configuração)  
- Docker  
- GitHub para versionamento  
- Dependências listadas no `requirements.txt`

---

## 📂 Estrutura do Projeto
```bash
backend-avancado-pokemon/
│
├── backend/ # Código fonte principal da API
│ ├── apis/ # Rotas / endpoints
│ │ ├── pokemon_apis.py
│ │ └── trainer_apis.py
│ │
│ ├── table/ # Modelos / definições de tabelas (schema)
│ │ ├── pokemon_table.py
│ │ └── trainer_table.py
│ │
│ ├── instance/ # Configurações de instância / ambiente
│ │ └── config.py
│ │
│ ├── test/ # Testes unitários ou de endpoints
│ │ └── test_pokemon.py
│ │
│ └── schema.py # Definições dos esquemas (pydantic ou marshmallow, etc.)
│
├── requirements.txt # Dependências do Python
├── README.md
└── Dockerfile # Containerização da API


---

## ⚙️ Instalação e Execução

### Pré-requisitos

- Python (versão X.X)  
- Docker (se for usar container)  
- Banco de dados suportado (SQLite/MySQL/PostgreSQL)  


### Localmente (sem Docker)

1. Clone este repositório  
   ```bash
   git clone https://github.com/HelenaMayumiTomokane/backend-avancado-pokemon.git
   cd backend-avancado-pokemon

2. Crie um ambiente virtual
    ```bash
    python -m venv venv

3. Ative um ambiente virtual
    ```bash
    source venv/bin/activate   # Linux/Mac
    .\venv\Scripts\activate    # Windows

4. Instale as dependências
    ```bash
    pip install -r requirements.txt

5. Execute a API
    ```bash
    python -m backend.app

### 🐳 Localmente (Com Docker)

1. Certifique-se de ter Docker instalado e rodando, caso não tenha, instale o Docker.
    ```bash
    ● Windows: https://docs.docker.com/desktop/install/windows-install/
    ● Ubuntu: https://docs.docker.com/engine/install/ubuntu/
    ● Mac OS: https://docs.docker.com/desktop/install/mac-install/

2. Na raiz do repositório, construa a imagem:
    ```bash
    docker build -t backend-pokemon .

3. Execute o container:
    ```bash
    docker run -d -p 5000:5000 backend-pokemon

4. Acesse via browser ou ferramenta de API:
    ```bash
    http://localhost:5000/openapi

---

### 🧭 Adição de Novas Tabelas / Rotas

Caso queira adicionar novos dados ou funcionalidade, siga este passo a passo:

1. Criar a tabela com suas colunas no folder table/

2. Criar as variáveis correspondentes no schema.py

3. Criar APIs de conexão com essa tabela no folder apis/

4. Adicionar o novo endpoint na aplicação principal (backend/app ou onde está o ponto de entrada)

5. Criar um teste correspondente no folder test/