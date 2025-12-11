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
├── backend/                        # Diretório principal do backend (Django)
│   ├── main/                       # Aplicação principal (App: "main")
│   │   ├── migrations/             # Histórico de alterações do banco de dados
│   │   ├── media/filmes/           # Local para upload de arquivos de mídia (ex: capas, trailers)
│   │   ├── static/                 # *Ausente na imagem, mas esperado em projetos Django
│   │   │   └── main/               # Arquivos estáticos (CSS, JS, Imagens)
│   │   ├── templates/main/         # Arquivos HTML/Templates
│   │   │   ├── add_filme.html      # Adicionar/Gerenciar filmes
│   │   │   ├── carrinho.html       # Visualização do carrinho
│   │   │   ├── detalhes.html       # Detalhes de um filme
│   │   │   ├── index.html          # Catálogo principal
│   │   │   ├── index_cadastro.html # Cadastro de usuário
│   │   │   ├── index_login.html    # Login de usuário
│   │   │   └── perfil.html         # Perfil/Biblioteca do usuário
│   │   ├── __init__.py             # Inicialização do módulo Python
│   │   ├── admin.py                # Configuração do painel administrativo
│   │   ├── apps.py                 # Configuração da aplicação 'main'
│   │   ├── forms.py                # Definição de formulários
│   │   ├── models.py               # Modelos do banco de dados (Usuário, Filme, etc.)
│   │   ├── signals.py              # Lógica para tratamento de Sinais do Django (ex: pós-salvamento)
│   │   ├── tests.py                # Testes unitários e funcionais da aplicação
│   │   ├── urls.py                 # Rotas/URLs do aplicativo 'main'
│   │   └── views.py                # Lógica de processamento de requisições
│   ├── myproject/                  # Configurações globais do projeto Django
│   │   ├── __init__.py             
│   │   ├── asgi.py                 # ASGI configuration
│   │   ├── settings.py             # Configurações gerais (DB, Apps, Media/Static URLs)
│   │   ├── urls.py                 # Roteamento principal
│   │   └── wsgi.py                 # WSGI configuration
│   ├── db.sqlite3                  # Banco de dados local (SQLite)
│   └── manage.py                   # Utilitário de linha de comando do Django
├── .gitignore                      # Arquivos ignorados pelo Git
├── Dockerfile                      # Definição da imagem Docker
├── Pipfile                         # Dependências do projeto (Pipenv)
├── Pipfile.lock                    # Versões fixadas das dependências
└── docker-compose.yml              # Orquestração do container Docker

