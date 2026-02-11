# Quick Reference - SaaS Conecta

Referência rápida para desenvolvimento diário.

---

## 🎯 Arquivos de Orientação

| Arquivo | Quando Usar |
|---------|-------------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Entender arquitetura geral |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Antes de contribuir |
| [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md) | Buscar componentes frontend |
| [.cursorrules](.cursorrules) | Lido automaticamente por AI |
| [scripts/README.md](scripts/README.md) | Rodar o projeto |

---

## 🚀 Comandos Mais Usados

### Rodar Projeto

```bash
# Local
./scripts/dev-local.sh

# Replit
# Apenas clique em "Run"
```

### Frontend

```bash
cd frontend

# Dev
bun dev

# Build
bun run build

# Limpar cache
rm -rf .nuxt .output
```

### Backend

```bash
cd backend
source ../env_conecta/bin/activate

# Migrations
python manage.py makemigrations
python manage.py migrate

# Admin
python manage.py createsuperuser

# Dev server
python manage.py runserver

# Shell
python manage.py shell
```

### Matar Processos

```bash
# Frontend (porta 3000)
lsof -ti :3000 | xargs kill -9

# Backend (porta 8000)
lsof -ti :8000 | xargs kill -9
```

---

## 📁 Estrutura Rápida

### Frontend

```
frontend/app/
├── components/
│   ├── Ui/              # Design System
│   └── [Feature]/       # Por feature
├── composables/         # Lógica reutilizável
├── pages/              # Rotas
├── services/           # API calls
├── stores/             # Pinia stores
└── utils/              # Funções utilitárias
```

### Backend

```
backend/app_name/
├── admin/              # Sempre subpasta
├── models/             # Sempre subpasta
├── serializers/        # Sempre subpasta
├── viewsets/           # Sempre subpasta
├── forms/              # Opcional
├── managers/           # Opcional
├── signals/            # Opcional
└── tests/              # Sempre subpasta
```

---

## 🎨 Componentes Mais Usados

### Frontend

```vue
<!-- Botão -->
<UiButton tipo="primary" size="md">Salvar</UiButton>

<!-- Input -->
<UiInput v-model="value" placeholder="Digite..." />

<!-- Empty State -->
<UiEmpty text="Nada encontrado" />

<!-- Quasar Badge -->
<q-badge label="Ativo" class="bg-primary" />

<!-- Scroll Area -->
<q-scroll-area class="h-full">
  <!-- conteúdo -->
</q-scroll-area>
```

### Tailwind Classes Úteis

```scss
// Layout
flex flex-col gap-16
grid grid-cols-3

// Responsivo
max-lg:hidden
max-sm:flex-col

// Cores (sistema custom)
bg-primary-pure
text-neutral-100
bg-neutral-20

// Spacing
p-24 mt-32 gap-16
```

---

## 🔧 Backend Patterns

### Model

```python
class MinhaModel(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )
    
    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )
    
    class Meta:
        verbose_name = 'Minha Model'
        verbose_name_plural = 'Minhas Models'
    
    def __str__(self):
        return self.nome
```

### Admin

```python
@admin.register(MinhaModel)
class MinhaModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo']
```

### Serializer

```python
class MinhaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinhaModel
        fields = '__all__'
```

### ViewSet

```python
class MinhaModelViewSet(NovadataModelViewSet):
    queryset = MinhaModel.objects.all()
    serializer_class = MinhaModelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['nome']
```

---

## 📡 API Proxy

Request no browser:
```
GET http://localhost:3000/api/vagas/
```

Middleware adiciona token:
```
Authorization: Token {API_SECRET}
```

Proxeia para backend:
```
GET http://localhost:8000/api/vagas/
```

**Config**: `frontend/server/middleware/api-proxy.js`

---

## ✅ Checklist Rápido

### Novo Componente Frontend

- [ ] Verificou se já existe?
- [ ] Usa componentes Ui/?
- [ ] Props bem definidos
- [ ] Responsivo
- [ ] Nome em PascalCase

### Novo Model Backend

- [ ] Criado em `models/[nome].py`
- [ ] Tem `verbose_name` em todos campos
- [ ] Admin configurado
- [ ] Serializer criado
- [ ] ViewSet criado
- [ ] URLs registrados
- [ ] Migrations criadas e aplicadas

---

## 🐛 Troubleshooting

### Frontend não carrega vagas

```bash
# 1. Verificar API
curl http://localhost:8000/api/vagas/

# 2. Verificar proxy
curl http://localhost:3000/api/vagas/

# 3. Limpar cache
cd frontend
rm -rf .nuxt .output

# 4. Reiniciar
./scripts/dev-local.sh
```

### Erro de autenticação

```bash
# Verificar token no .env
cat frontend/.env | grep API_SECRET

# Verificar no Django Admin
# http://localhost:8000/admin/authtoken/tokenproxy/
```

### Migration error

```bash
cd backend
python manage.py migrate --fake [app_name] zero
python manage.py migrate [app_name]
```

---

## 🔑 Variáveis de Ambiente

### Frontend (.env)

```env
API_SECRET=token-django
API_URL=http://localhost:8000
NUXT_PUBLIC_APP_URL=http://localhost:3000
```

### Backend

Configurado via Django settings ou variáveis de ambiente.

---

## 📚 Documentação Completa

Leia os arquivos principais:

1. **[ARCHITECTURE.md](ARCHITECTURE.md)** - Arquitetura detalhada
2. **[CONTRIBUTING.md](CONTRIBUTING.md)** - Como contribuir
3. **[DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)** - Componentes disponíveis

---

## 💡 Dicas

- Use `console.log` para debug no frontend
- Use `print()` ou Django shell para debug no backend
- Veja código similar antes de criar algo novo
- Mantenha componentes pequenos e focados
- Documente decisões importantes

---

**Este é um guia vivo. Atualize conforme o projeto evolui!**
