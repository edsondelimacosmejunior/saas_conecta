# Scripts de Desenvolvimento

## dev-local.sh

Script para rodar o ambiente de desenvolvimento completo (Backend Django + Frontend Nuxt) **localmente**.

### Uso

```bash
# Do diretório raiz do projeto
./scripts/dev-local.sh
```

### O que o script faz:

1. **Ativa o virtualenv Python** (`env_conecta`)
2. **Instala dependências** do backend
3. **Executa migrations** do Django
4. **Inicia Django** em `http://localhost:8000`
5. **Configura variáveis de ambiente** para o frontend (.env)
6. **Instala dependências** do frontend (bun)
7. **Inicia Nuxt** em `http://localhost:3000`

### Proxy API

O frontend Nuxt faz proxy automático de todas as requisições `/api/*` para o Django backend usando o middleware em `frontend/server/middleware/api-proxy.js`.

- Requisições no browser: `http://localhost:3000/api/vagas/`
- São redirecionadas para: `http://localhost:8000/api/vagas/`
- Com header: `Authorization: Token {API_SECRET}`

### Variáveis de Ambiente

Você pode customizar as variáveis antes de rodar o script:

```bash
export API_SECRET="seu-token-aqui"
export API_URL="http://localhost:8000"
export PORT="3000"
./scripts/dev-local.sh
```

### Parar os servidores

Pressione `Ctrl+C` - o script irá encerrar automaticamente todos os processos.

---

## replit-dev.sh

Script otimizado para rodar no **Replit** com suporte para URLs dinâmicas.

### Configuração no Replit

O arquivo `.replit` já está configurado para rodar este script automaticamente:

```plaintext
run = "bash scripts/replit-dev.sh"
```

Basta clicar em **Run** no Replit!

### O que o script faz:

1. **Detecta ambiente Replit** automaticamente (via `REPL_SLUG` e `REPL_OWNER`)
2. **Configura URL pública** dinâmica do Replit
3. **Instala dependências** do Django
4. **Executa migrations**
5. **Inicia Django** em `http://0.0.0.0:8000`
6. **Cria .env** do frontend com configurações corretas
7. **Instala dependências** do Nuxt (apenas se necessário)
8. **Inicia Nuxt** com proxy configurado

### URLs no Replit

- **Frontend público**: `https://{REPL_SLUG}.{REPL_OWNER}.repl.co`
- **Backend interno**: `http://0.0.0.0:8000`
- **Proxy**: `/api/*` → Backend Django com token automático

### Variáveis de Ambiente no Replit

Configure nos **Secrets** do Replit (opcional):

- `API_SECRET` - Token de autenticação da API (padrão já incluído)
- `API_URL` - URL do backend (padrão: `http://0.0.0.0:8000`)

### Otimizações

- **Cache de dependências**: Só reinstala se `package.json` mudou
- **Output colorido**: Feedback visual do status de cada serviço
- **Cleanup automático**: Encerra processos corretamente ao parar

---

## Como funciona o Proxy

Ambos os scripts configuram o mesmo sistema de proxy:

```
Browser → http://localhost:3000/api/vagas/
         ↓
    Nuxt Middleware (server/middleware/api-proxy.js)
         ↓
    Adiciona: Authorization: Token {API_SECRET}
         ↓
    Django → http://localhost:8000/api/vagas/
```

Isso permite que o frontend acesse a API autenticada sem expor credenciais no browser.
