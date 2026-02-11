#!/usr/bin/env bash
set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔷 Replit Development Environment${NC}"
echo -e "${GREEN}🚀 Iniciando Backend e Frontend...${NC}\n"

# Variáveis de ambiente para Replit
export PYTHONUNBUFFERED=1
export API_SECRET="${API_SECRET:-a751cdd6e7334ae9fe6f5450d71f2d4e3efd3c18}"
export API_URL="${API_URL:-http://0.0.0.0:8000}"
export PORT="${PORT:-3000}"

# No Replit, a URL pública é dinâmica
if [ -n "$REPL_SLUG" ] && [ -n "$REPL_OWNER" ]; then
  export NUXT_PUBLIC_APP_URL="https://${REPL_SLUG}.${REPL_OWNER}.repl.co"
  echo -e "${BLUE}📡 Replit URL: ${NUXT_PUBLIC_APP_URL}${NC}"
else
  export NUXT_PUBLIC_APP_URL="http://localhost:3000"
fi

# Cleanup ao sair
cleanup() {
  echo -e "\n${YELLOW}🛑 Encerrando servidores...${NC}"
  pkill -P $$ || true
  exit 0
}
trap cleanup SIGINT SIGTERM EXIT

# --- Backend (Django) ---
echo -e "${GREEN}📦 Backend Django...${NC}"
pip install -q -r backend/requirements.txt
cd backend
python manage.py migrate --noinput 2>/dev/null || true
echo -e "${GREEN}✅ Django: http://0.0.0.0:8000${NC}"
python manage.py runserver 0.0.0.0:8000 &
DJANGO_PID=$!
cd ..

# Aguardar Django estar pronto
sleep 3

# --- Frontend (Nuxt) ---
echo -e "${GREEN}⚡ Frontend Nuxt...${NC}"
cd frontend

# Criar .env com as variáveis corretas
cat > .env << EOF
API_SECRET=${API_SECRET}
API_URL=${API_URL}
NUXT_PUBLIC_APP_URL=${NUXT_PUBLIC_APP_URL}
EOF

# No Replit, instalar deps apenas se mudou
if [ ! -d "node_modules" ] || [ "package.json" -nt "node_modules" ]; then
  echo -e "${YELLOW}📦 Instalando dependências...${NC}"
  bun install
fi

echo -e "${GREEN}✅ Nuxt: ${NUXT_PUBLIC_APP_URL}${NC}"
echo -e "${YELLOW}📡 Proxy /api → ${API_URL}${NC}\n"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

bun dev

# Manter script rodando
wait $DJANGO_PID
