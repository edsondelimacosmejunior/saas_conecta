# SaaS Conecta

Plataforma de recrutamento com Django (Backend) + Nuxt 3 (Frontend).

---

## 📚 Documentação Essencial

**LEIA ANTES DE DESENVOLVER**:

- 📖 **[ARCHITECTURE.md](ARCHITECTURE.md)** - Arquitetura completa do projeto
- 🤖 **[.cursorrules](.cursorrules)** - Regras de desenvolvimento (lido por AI assistants)
- 🤝 **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guia de contribuição
- 🎨 **[DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)** - Componentes e Design System
- ⚡ **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Referência rápida
- 📜 **[scripts/README.md](scripts/README.md)** - Documentação dos scripts

---

## 🚀 Quick Start

### Desenvolvimento Local

```bash
# Clonar o repositório
git clone <repo-url>
cd saas_conecta

# Rodar tudo de uma vez
./scripts/dev-local.sh
```

Acesse:
- **Frontend**: http://localhost:3000
- **Backend Admin**: http://localhost:8000/admin
- **API**: http://localhost:8000/api

### No Replit

1. Abra o projeto no Replit
2. Clique em **Run** (ou pressione `Ctrl+Enter`)
3. Acesse a URL pública gerada

## 📁 Estrutura do Projeto

```
saas_conecta/
├── backend/           # Django REST API
│   ├── conecta/      # Configurações
│   ├── home/         # App principal
│   └── recrutamento/ # App de vagas e candidatos
├── frontend/         # Nuxt 3 Application
│   ├── app/          # Código fonte
│   ├── server/       # Server middleware (proxy)
│   └── .env          # Variáveis de ambiente
└── scripts/          # Scripts de desenvolvimento
    ├── dev-local.sh  # Para rodar localmente
    └── replit-dev.sh # Para rodar no Replit
```

## 🔧 Configuração Manual

### Backend (Django)

```bash
# Criar virtualenv
python3 -m venv env_conecta
source env_conecta/bin/activate

# Instalar dependências
pip install -r backend/requirements.txt

# Migrations
cd backend
python manage.py migrate

# Criar superuser
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver
```

### Frontend (Nuxt)

```bash
cd frontend

# Configurar .env
cp .env.example .env

# Instalar dependências
bun install

# Rodar dev server
bun dev
```

## 🔐 Variáveis de Ambiente

### Frontend (.env)

```env
API_SECRET=a751cdd6e7334ae9fe6f5450d71f2d4e3efd3c18
API_URL=http://localhost:8000
NUXT_PUBLIC_APP_URL=http://localhost:3000
```

## 📡 Proxy API

O frontend usa um middleware em `frontend/server/middleware/api-proxy.js` que:

1. Intercepta todas as requisições `/api/*`
2. Adiciona o header `Authorization: Token {API_SECRET}`
3. Redireciona para o Django backend

Isso permite acesso autenticado à API sem expor credenciais no browser.

## 🛠️ Comandos Úteis

```bash
# Matar processos nas portas
lsof -ti :3000 | xargs kill -9  # Frontend
lsof -ti :8000 | xargs kill -9  # Backend

# Ver logs do Django
cd backend && python manage.py runserver --verbosity 2

# Build do frontend
cd frontend && bun run build

# Rodar testes
cd backend && python manage.py test
```

## 📚 Documentação

- [Scripts de Desenvolvimento](scripts/README.md)
- [Documentação do Backend](backend/README.md)
- [Documentação do Frontend](frontend/README.md)

## 🐛 Troubleshooting

### Vagas não aparecem no frontend?

1. Verifique se o backend está rodando: `curl http://localhost:8000/api/vagas/`
2. Verifique se o proxy está funcionando: `curl http://localhost:3000/api/vagas/`
3. Limpe o cache do Nuxt: `rm -rf frontend/.nuxt frontend/.output`
4. Reinicie os servidores

### Erro de autenticação na API?

Verifique se o `API_SECRET` no `frontend/.env` corresponde a um token válido no Django admin.
