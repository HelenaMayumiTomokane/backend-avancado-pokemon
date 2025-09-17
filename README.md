# Backend Avançado Pokémon

## 📖 Descrição

Este é o módulo **API principal** de um sistema inspirado no universo Pokémon. Ele serve para gerenciar dados de Pokémons, fornecendo endpoints REST para CRUD. Desenvolvido em Python com Flask, com persistência em banco de dados.  

---

## 📦 Funcionalidades Principais

- Listar, criar, atualizar e deletar Pokémons, Usuários, Cash e Itens (`GET`, `POST`, `PUT`, `DELETE`)
- Testes de rotas principais
- Documentação automática via OpenAPI/Swagger pelo 
    ```bash 
    http://127.0.0.1:5000/openapi

---

## 💻 Tecnologias

- 🐍 **Python**  
- 🌐 **Flask**  
- 🗄️ **SQLite**  
- 🐳 **Docker**  
- 🏷️ **GitHub** para versionamento  
- 📦 Dependências listadas no `requirements.txt`


---

## 📂 Estrutura do Projeto
```
backend-avancado-pokemon/
│
├── backend/                        # Código fonte principal da API
│   ├── pokemon/                    # Módulo Pokémon
│   │   ├── apis/                   # Rotas / endpoints da API
│   │   │   ├── __init__.py
│   │   │   ├── account_user_api.py
│   │   │   ├── cash_audit_api.py
│   │   │   ├── owner_pokemon_api.py
│   │   │   └── user_bag_api.py
│   │   │
│   │   ├── tables/                 # Modelos / definições das tabelas do banco
│   │   │   ├── __init__.py
│   │   │   ├── account_user.py
│   │   │   ├── cash_audit.py
│   │   │   ├── owner_pokemon.py
│   │   │   └── user_bag.py
│   │   │
│   │   ├── instance/               # Arquivos de configuração / banco de dados local
│   │   │   └── database.db
│   │   │
│   │   ├── test/                   # Testes unitários ou de integração
│   │   │   ├── __init__.py
│   │   │   ├── account_user_test.py
│   │   │   ├── cash_audit_test.py
│   │   │   ├── owner_pokemon_test.py
│   │   │   └── user_bag_test.py
│   │   │
│   │   ├── __init__.py             # Inicialização do pacote Python
│   │   ├── schema.py               # Schemas Pydantic (validação de dados)
│   │   ├── error_schema.py         # Schemas para erros e respostas padronizadas
│   │   ├── database.py             # Conexão e manipulação do banco de dados
│   │   ├── config.py               # Configurações gerais da aplicação
│   │   └── app.py                  # Ponto de entrada da API (FastAPI / Flask)
│   │
│   ├── docker-compose.yml          # Orquestração de containers da aplicação (API, banco de dados, etc.)
│   ├── requirements.txt            # Dependências do Python
│   ├── README.md                   # Documentação da API
│   └── Dockerfile                  # Containerização da API

```

---

## ⚙️ Instalação e Execução

### Pré-requisitos

- 🐍 **Python** + **Flask** para o backend.
- 🗄️ **SQLAlchemy** para banco de dados.
- 🐳 **Docker** para containerização da aplicação (opcional, mas recomendado).
- 📦 **Docker Compose** para orquestrar múltiplos containers (API + banco de dados e frontend).


### Localmente (sem Docker)

1. Clone este repositório  
   ```bash
   git clone https://github.com/HelenaMayumiTomokane/backend-avancado-pokemon.git
   cd backend-avancado-pokemon

2. Crie um Ambiente Virtual
    ```bash
    py -m venv venv 

3. Ativar o Ambiente Virtual => no Windows
     ```bash 
    venv\Scripts\Activate 
    
4. Instale as dependências
    ```bash
    pip install -r requirements.txt

5. Execute a API
    ```bash
    python -m backend.app

### 🐳 Localmente (Com Docker)
1. Clone este repositório  
   ```bash
   git clone https://github.com/HelenaMayumiTomokane/backend-avancado-pokemon.git
   cd backend-avancado-pokemon

2. Certifique-se de ter Docker instalado e rodando, caso não tenha, instale o Docker.
    - Windows: 
        https://docs.docker.com/desktop/install/windows-install/

    - Ubuntu: 
        https://docs.docker.com/engine/install/ubuntu/

    - Mac OS: 
        https://docs.docker.com/desktop/install/mac-in

3. Na raiz do repositório, construa a imagem:
    ```bash
    docker build -t backend-pokemon .

4. Execute o container:
    ```bash
    docker run -d -p 5000:5000 backend-pokemon

5. Acesse via browser ou ferramenta de API:
    ```bash
    http://localhost:5000/openapi

### 🐳 Localmente (Com Docker Compose)
1. Clone este repositório  
   ```bash
   git clone https://github.com/HelenaMayumiTomokane/backend-avancado-pokemon.git
   cd backend-avancado-pokemon

2. Certifique-se de ter Docker instalado e rodando, caso não tenha, instale o Docker.
    - Windows: 
        https://docs.docker.com/desktop/install/windows-install/

    - Ubuntu: 
        https://docs.docker.com/engine/install/ubuntu/

    - Mac OS: 
        https://docs.docker.com/desktop/install/mac-in

3. Na raiz do repositório, suba os serviços definidos no `docker-compose.yml`:  
   ```bash
   docker-compose up -d

4. Para parar os serviços:
    ```bash
    docker-compose down