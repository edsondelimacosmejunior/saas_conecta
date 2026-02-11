#!/usr/bin/env bash
set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Iniciando ambiente de desenvolvimento${NC}"

# Garantir que estamos no diretório raiz do projeto
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Variáveis de ambiente
export PYTHONUNBUFFERED=1
export API_SECRET="${API_SECRET:-a751cdd6e7334ae9fe6f5450d71f2d4e3efd3c18}"
export API_URL="${API_URL:-http://localhost:8000}"
export PORT="${PORT:-3000}"

# Cleanup ao sair
cleanup() {
  echo -e "\n${YELLOW}🛑 Encerrando servidores...${NC}"
  pkill -P $$ || true
  lsof -ti :8000 | xargs kill -9 2>/dev/null || true
  lsof -ti :3000 | xargs kill -9 2>/dev/null || true
  exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# --- Backend (Django) ---
echo -e "${GREEN}📦 Configurando Backend Django...${NC}"
if [ -d "env_conecta" ]; then
  source env_conecta/bin/activate
else
  echo -e "${YELLOW}⚠️  Virtualenv não encontrado, criando...${NC}"
  python3 -m venv env_conecta
  source env_conecta/bin/activate
fi

pip install -q -r backend/requirements.txt
cd backend
python manage.py migrate --noinput 2>/dev/null || true
echo -e "${GREEN}✅ Django rodando em http://localhost:8000${NC}"
python manage.py runserver 0.0.0.0:8000 &
DJANGO_PID=$!
cd ..

# Aguardar Django estar pronto
sleep 3

# --- Frontend (Nuxt) ---
echo -e "${GREEN}⚡ Configurando Frontend Nuxt...${NC}"
cd frontend

# Criar/atualizar .env
cat > .env << EOF
API_SECRET=${API_SECRET}
API_URL=${API_URL}
EOF

bun install
echo -e "${GREEN}✅ Nuxt rodando em http://localhost:3000${NC}"
echo -e "${YELLOW}📡 Proxy /api -> ${API_URL}${NC}\n"
bun dev

# Manter script rodando
wait $DJANGO_PID
