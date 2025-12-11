# Locadora de Filmes Online

Este é um projeto acadêmico de **Engenharia de Software**, cujo objetivo é desenvolver um **MVP (Minimum Viable Product)** de uma locadora de filmes online.  

O sistema permite que usuários possam:  
- Criar conta e realizar login  
- Navegar pelo catálogo de filmes  
- Adicionar/remover filmes do carrinho  
- Adicionar filme na biblioteca e remover filme da biblioteca  


##  Tecnologias Utilizadas

### Para o desenvolvimento foi utilizado o Docker
### Frontend
- Criação das interfaces (HTML, CSS e JS).  

### Backend
- **Django (Python)** → responsável pela lógica do sistema e API.  
- **Foi utilizado o SQLite do próprio django** → criação dos endpoints (CRUD de usuários, filmes e carrinho).

### Pré-requisitos
* [Docker](https://www.docker.com/) (para rodar via container)
  
### Rodando com Docker

Após ter clonado o repositório usando git ou via GUI no site do projeto, certifique-se de ter o docker baixado e iniciado, em seguida, basta navegar até a pasta onde escontra-se o arquivo "Dockerfile" e executar no terminal: docker compose up --build.
Depois, entre no campo de busca do navegador e pesquise por: localhost:8000.

##  Estrutura do Projeto

```text
Projeto_completo/
├── backend/                    # Diretório principal do backend (Django)
│   ├── main/                   # Aplicação principal (App)
│   │   ├── migrations/         # Histórico de alterações do banco de dados
│   │   ├── static/main/        # Arquivos estáticos
│   │   │   ├── css/            # Estilos (ex: carrosel.css, style.css)
│   │   │   ├── imagens/        # Imagens do projeto
│   │   │   └── js/             # Scripts JavaScript
│   │   ├── templates/main/     # Arquivos HTML
│   │   │   ├── index.html      # Página inicial
│   │   │   ├── index_cadastro.html
│   │   │   ├── index_login.html
│   │   │   └── trailer.html
│   │   ├── admin.py            # Configuração do painel administrativo
│   │   ├── forms.py            # Definição de formulários
│   │   ├── models.py           # Modelos do banco de dados
│   │   ├── urls.py             # Rotas específicas do app 'main'
│   │   └── views.py            # Lógica das views
│   ├── myproject/              # Configurações globais do projeto Django
│   │   ├── settings.py         # Configurações gerais (Apps, DB, Middleware)
│   │   ├── urls.py             # Roteamento principal de URLs
│   │   └── wsgi.py             # Interface gateway para deploy
│   ├── db.sqlite3              # Banco de dados local (SQLite)
│   └── manage.py               # Utilitário de linha de comando do Django
├── .gitignore                  # Arquivos ignorados pelo Git
├── docker-compose.yml          # Orquestração de containers Docker
├── Dockerfile                  # Definição da imagem Docker
├── Pipfile                     # Dependências do ambiente virtual (Pipenv)

