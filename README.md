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
│   ├── main/                       # Aplicação principal (App)
│   │   ├── migrations/             # Histórico de alterações do banco de dados (ex: 0001_initial.py)
│   │   ├── static/main/            # Arquivos estáticos
│   │   │   ├── css/                # Estilos CSS (carrosel.css, style.css, reset.css)
│   │   │   ├── imagens/            # Imagens do projeto (capas de filmes, ícones, logos)
│   │   │   └── js/                 # Scripts JavaScript (script.js, user.js, ajax_requests.js)
│   │   ├── templates/main/         # Arquivos HTML/Templates (Interface do Usuário)
│   │   │   ├── add_filme.html      # Página para adicionar/gerenciar filmes (se for Admin)
│   │   │   ├── carrinho.html       # Visualização e gestão dos filmes selecionados
│   │   │   ├── detalhes.html       # Página de detalhes de um filme específico
│   │   │   ├── index.html          # Página inicial/catálogo de filmes
│   │   │   ├── index_cadastro.html # Página para cadastro de novos usuários
│   │   │   ├── index_login.html    # Página para autenticação/login de usuários
│   │   │   ├── index_trailer.html  # Página ou modal para exibição de trailer
│   │   │   ├── perfil.html         # Página de perfil do usuário e sua biblioteca
│   │   ├── __init__.py             # Inicialização do módulo Python
│   │   ├── admin.py                # Configuração do painel administrativo do Django
│   │   ├── apps.py                 # Configuração da aplicação 'main'
│   │   ├── forms.py                # Definição de formulários (ex: UserForm, LoginForm, FilmeForm)
│   │   ├── models.py               # Modelos do banco de dados (Usuario, Filme, Carrinho, Biblioteca)
│   │   ├── urls.py                 # Rotas/URLs específicas do app 'main'
│   │   └── views.py                # Lógica das views (funções que processam requisições)
│   ├── myproject/                  # Configurações globais do projeto Django
│   │   ├── __init__.py             
│   │   ├── asgi.py                 # Interface gateway assíncrona
│   │   ├── settings.py             # Configurações gerais (Apps, DB, Middleware, Static Files)
│   │   ├── urls.py                 # Roteamento principal de URLs (inclui as rotas do app 'main')
│   │   └── wsgi.py                 # Interface gateway para deploy (padrão)
│   ├── db.sqlite3                  # Banco de dados local (SQLite)
│   └── manage.py                   # Utilitário de linha de comando do Django
├── .gitignore                      # Arquivos ignorados pelo Git (incluir db.sqlite3, __pycache__)
├── docker-compose.yml              # Orquestração do serviço web (Django) no container
├── Dockerfile                      # Definição da imagem Docker (instalação de dependências Python/Django)
├── Pipfile                         # Dependências do ambiente virtual (Pipenv)
└── Pipfile.lock                    # Hash de dependências fixadas (para reprodutibilidade)

