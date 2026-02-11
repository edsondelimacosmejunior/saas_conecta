# Arquitetura do Projeto - SaaS Conecta

## Visão Geral

Monorepo com:
- **Backend**: Django REST Framework
- **Frontend**: Nuxt 3 + Quasar + TailwindCSS
- **Deploy**: Netlify (Frontend) + Railway/Heroku (Backend)
- **Dev**: Scripts unificados para Replit e local

---

## Design System (Frontend)

### Princípios

1. **Reuso acima de tudo**: Sempre use componentes existentes
2. **Composição**: Componentes pequenos e combináveis
3. **Props-driven**: Configuração via props, não hardcode
4. **Responsivo**: Mobile-first com Tailwind

### Componentes Base

Localização: `frontend/app/components/Ui/`

| Componente | Uso | Props principais |
|------------|-----|------------------|
| `UiButton` | Botões e ações | `tipo`, `size`, `label` |
| `UiInput` | Inputs de formulário | `modelValue`, `placeholder`, `size` |
| `UiEmpty` | Estados vazios | `text`, `icon` |

### Componentes de Feature

Localização: `frontend/app/components/[Feature]/`

Exemplos:
- `Vaga/VagaCard.vue` - Card de vaga
- `Vaga/VagaAttributes.vue` - Atributos da vaga
- `Vaga/VagaDescription.vue` - Descrição da vaga

### Como Criar Componente Novo

```vue
<!-- frontend/app/components/Ui/UiNovoComponente.vue -->
<script setup>
defineProps({
  // Props com tipos e defaults
  label: {
    type: String,
    default: ''
  },
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary'].includes(v)
  }
})
</script>

<template>
  <!-- Template reutilizável -->
</template>

<style scoped>
/* Estilos apenas se necessário */
</style>
```

---

## Estrutura Backend (Django)

### Organização de Apps

Cada app Django tem estrutura FIXA:

```
app_name/
├── admin/
│   ├── __init__.py           # Imports e registros
│   └── model_admin.py        # Admin de cada model
├── models/
│   ├── __init__.py           # Imports de models
│   └── model.py              # Definição do model
├── serializers/
│   ├── __init__.py           # Imports
│   └── model_serializers.py  # Serializers
├── viewsets/
│   ├── __init__.py           # Imports
│   └── model_viewsets.py     # ViewSets
├── forms/                    # Opcional
├── managers/                 # Opcional - Custom managers
├── signals/                  # Opcional - Django signals
├── migrations/               # Auto-gerado
├── static/                   # Arquivos estáticos do app
├── templates/                # Templates Django
├── tests/                    # Testes organizados
│   ├── models/
│   ├── admin/
│   └── viewsets/
├── apps.py
└── urls.py
```

### Exemplo: Model

```python
# recrutamento/models/vaga.py
from django.db import models
from django_editorjs import EditorJsField

class Vaga(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
    )
    
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=100,
        unique=True,
    )
    
    sobre = EditorJsField(
        verbose_name='Sobre a Vaga',
        blank=True,
        null=True,
    )
    
    ativa = models.BooleanField(
        verbose_name='Ativa',
        default=True,
    )
    
    # Campos de auditoria
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    usuario_criacao = models.ForeignKey(
        'home.Usuario',
        on_delete=models.PROTECT,
        related_name='+',
    )
    
    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.titulo
```

### Exemplo: Admin

```python
# recrutamento/admin/vaga_admin.py
from django.contrib import admin
from ..models import Vaga

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = [
        'titulo',
        'ativa',
        'data_fechamento',
        'data_criacao',
    ]
    
    list_filter = [
        'ativa',
        'tipo_contratacao',
        'area_atuacao',
    ]
    
    search_fields = [
        'titulo',
        'slug',
    ]
    
    prepopulated_fields = {
        'slug': ('titulo',)
    }
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'slug', 'ativa')
        }),
        ('Conteúdo', {
            'fields': ('sobre', 'responsabilidades')
        }),
        ('Detalhes', {
            'fields': ('salario', 'tipo_contratacao', 'area_atuacao')
        }),
    )
```

### Exemplo: Serializer

```python
# recrutamento/serializers/vaga_serializers.py
from rest_framework import serializers
from ..models import Vaga

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = [
            'id',
            'titulo',
            'slug',
            'sobre',
            'ativa',
            'responsabilidades',
            'data_fechamento',
            'salario',
            'tipo_contratacao',
            'area_atuacao',
            'data_criacao',
            'data_atualizacao',
        ]
```

### Exemplo: ViewSet

```python
# recrutamento/viewsets/vaga_viewsets.py
from novadata_utils.viewsets import NovadataModelViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Vaga
from ..serializers import VagaSerializer

class VagaViewSet(NovadataModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    permission_classes = [AllowAny]  # Público
    http_method_names = ["get", "head", "options"]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    filterset_fields = [
        'slug',
        'ativa',
        'tipo_contratacao',
        'area_atuacao',
    ]
    
    search_fields = ['titulo']
```

---

## Proxy de API

### Como Funciona

1. Frontend faz request: `GET http://localhost:3000/api/vagas/`
2. Middleware Nuxt (`server/middleware/api-proxy.js`) intercepta
3. Adiciona header: `Authorization: Token {API_SECRET}`
4. Proxeia para: `GET http://localhost:8000/api/vagas/`
5. Retorna resposta ao browser

### Configuração

**Frontend** (`frontend/.env`):
```env
API_SECRET=token-da-api-django
API_URL=http://localhost:8000
```

**Backend**: Token gerado via Django Admin → Authentication → Tokens

---

## Fluxo de Desenvolvimento

### Nova Feature no Frontend

1. ✅ Verificar componentes existentes
2. ✅ Criar composable se necessário (`composables/`)
3. ✅ Criar service se chamar API (`services/`)
4. ✅ Criar componentes reutilizáveis (`components/`)
5. ✅ Criar página (`pages/`)
6. ✅ Testar localmente

### Nova Feature no Backend

1. ✅ Criar/modificar model (`models/`)
2. ✅ Criar migrations: `python manage.py makemigrations`
3. ✅ Criar admin (`admin/`)
4. ✅ Criar serializer (`serializers/`)
5. ✅ Criar viewset (`viewsets/`)
6. ✅ Adicionar rota no `urls.py`
7. ✅ Testar via Django Admin e API
8. ✅ Rodar migrations: `python manage.py migrate`

### Novo App Django

```bash
# Criar app
python manage.py startapp novo_app

# Organizar estrutura
cd novo_app
mkdir admin models serializers viewsets forms managers signals tests
touch admin/__init__.py models/__init__.py serializers/__init__.py viewsets/__init__.py

# Mover arquivos
mv models.py models/
mv admin.py admin/

# Deletar arquivos não usados
rm views.py

# Adicionar em settings.py
INSTALLED_APPS += ['novo_app']

# Configurar URLs
```

---

## Padrões de Código

### Python (Backend)

- **PEP 8**: Formatação padrão Python
- **Type hints**: Sempre que possível
- **Docstrings**: Para funções públicas
- **Imports**: Absolutos, organizados (stdlib, third-party, local)

### JavaScript/Vue (Frontend)

- **ES6+**: Arrow functions, destructuring, etc.
- **Composition API**: Usar `<script setup>`
- **TypeScript**: Opcional, mas recomendado para utils
- **Async/Await**: Preferir sobre `.then()`

---

## Performance

### Frontend

- ✅ SSR desabilitado para páginas dinâmicas
- ✅ Lazy loading de componentes pesados
- ✅ Otimização de imagens
- ✅ Cache de API com `useAsyncData`

### Backend

- ✅ Select related / Prefetch related em queries
- ✅ Índices em campos filtráveis
- ✅ Paginação padrão configurada
- ✅ Cache de queries frequentes

---

## Segurança

### Frontend

- ✅ Token NUNCA exposto no browser
- ✅ Proxy server-side para API
- ✅ Sanitização de inputs
- ✅ HTTPS em produção

### Backend

- ✅ CSRF protection habilitado
- ✅ CORS configurado corretamente
- ✅ Rate limiting em APIs públicas
- ✅ Validação em serializers
- ✅ Permissions em todos viewsets

---

## Referências Rápidas

### Comandos Úteis

```bash
# Backend
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# Frontend
bun install
bun dev
bun run build

# Ambos
./scripts/dev-local.sh     # Local
./scripts/replit-dev.sh    # Replit
```

### Estrutura de Importação

**Frontend**:
```vue
<script setup>
// Services
import { vagasService } from '~/services/vagas.service'

// Composables (auto-imported)
const { data } = useAsyncData()
const showError = useShowError()

// Components (auto-imported se em components/)
</script>
```

**Backend**:
```python
# Imports do próprio app
from ..models import Vaga
from ..serializers import VagaSerializer

# Imports de outros apps
from home.models import Usuario

# Imports de packages
from django.db import models
from rest_framework import serializers
```

---

Esta arquitetura foi projetada para:
- 🚀 **Velocidade**: Desenvolvimento rápido com componentes prontos
- 🔧 **Manutenibilidade**: Padrões claros e consistentes
- 📈 **Escalabilidade**: Estrutura que cresce sem bagunça
- 👥 **Colaboração**: Fácil para novos devs entenderem
