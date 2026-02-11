# Guia de Contribuição - SaaS Conecta

## 📋 Antes de Começar

**LEIA OBRIGATORIAMENTE**:

1. [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitetura e padrões do projeto
2. [.cursorrules](.cursorrules) - Regras de desenvolvimento
3. [scripts/README.md](scripts/README.md) - Como rodar o projeto

---

## 🎯 Filosofia do Projeto

### Design System First

- ✅ **SEMPRE** use componentes do Design System existentes
- ✅ **NUNCA** crie UI do zero sem verificar componentes disponíveis
- ✅ Novos componentes devem ser **genéricos e reutilizáveis**
- ✅ Adicione ao Storybook (se disponível)

### Backend Consistente

- ✅ Siga a estrutura de pastas **EXATAMENTE** como apps existentes
- ✅ Models, Admin, Serializers, ViewSets em **pastas separadas**
- ✅ Use os mesmos padrões de nomenclatura
- ✅ Mantenha imports organizados nos `__init__.py`

---

## 🚀 Setup do Ambiente

### Local

```bash
# Clone o projeto
git clone <repo-url>
cd saas_conecta

# Rode o script de desenvolvimento
./scripts/dev-local.sh
```

### Replit

1. Abra o projeto no Replit
2. Aguarde instalação automática
3. Clique em **Run**

---

## 📝 Workflow de Desenvolvimento

### Para Features de Frontend

**1. Planejamento**
- [ ] Verificar componentes existentes em `frontend/app/components/`
- [ ] Identificar composables reutilizáveis em `frontend/app/composables/`
- [ ] Verificar se precisa de novo service em `frontend/app/services/`

**2. Desenvolvimento**
```bash
# Se precisa criar componente
touch frontend/app/components/[Feature]/NovoComponente.vue

# Se precisa criar service
touch frontend/app/services/novo.service.js

# Se precisa criar composable
touch frontend/app/composables/useNovo.js
```

**3. Checklist**
- [ ] Componente usa props (não hardcode)
- [ ] Componente é responsivo (Tailwind classes)
- [ ] Reutiliza componentes Ui/ quando possível
- [ ] Código está limpo e documentado
- [ ] Testado em diferentes tamanhos de tela

### Para Features de Backend

**1. Planejamento**
- [ ] Verificar se app apropriado existe
- [ ] Se novo app necessário, seguir estrutura padrão
- [ ] Identificar models relacionados

**2. Desenvolvimento**

```bash
# Criar model
touch backend/app_name/models/novo_model.py

# Criar migrations
python backend/manage.py makemigrations

# Criar admin
touch backend/app_name/admin/novo_model_admin.py

# Criar serializer
touch backend/app_name/serializers/novo_model_serializers.py

# Criar viewset
touch backend/app_name/viewsets/novo_model_viewsets.py

# Aplicar migrations
python backend/manage.py migrate
```

**3. Checklist**
- [ ] Model tem `verbose_name` em todos campos
- [ ] Admin configurado com `list_display`, `search_fields`, `list_filter`
- [ ] Serializer com todos campos necessários
- [ ] ViewSet com `permission_classes` definido
- [ ] URLs configurados corretamente
- [ ] Testado via Django Admin
- [ ] Testado via API

---

## 📁 Estrutura de Arquivos

### Criar Novo Componente Frontend

```vue
<!-- frontend/app/components/[Feature]/ComponenteNovo.vue -->
<script setup>
/**
 * Descrição do componente
 * @component ComponenteNovo
 */

// Props com validação
const props = defineProps({
  item: {
    type: Object,
    required: true
  },
  variant: {
    type: String,
    default: 'primary',
    validator: (v) => ['primary', 'secondary'].includes(v)
  }
})

// Emits documentados
const emit = defineEmits(['click', 'update'])

// Composables
const { data } = useAsyncData()
</script>

<template>
  <div class="componente-wrapper">
    <!-- Use componentes do Design System -->
    <UiButton @click="emit('click')">
      {{ item.label }}
    </UiButton>
  </div>
</template>

<style scoped>
/* Apenas se absolutamente necessário */
</style>
```

### Criar Novo Model Django

```python
# backend/app_name/models/novo_model.py
from django.db import models
from crum import get_current_user

class NovoModel(models.Model):
    """
    Descrição do model
    """
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )
    
    ativo = models.BooleanField(
        verbose_name='Ativo',
        default=True,
    )
    
    # Campos de auditoria
    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True
    )
    
    data_atualizacao = models.DateTimeField(
        verbose_name='Data de Atualização',
        auto_now=True
    )
    
    usuario_criacao = models.ForeignKey(
        'home.Usuario',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='Usuário de Criação',
    )
    
    usuario_atualizacao = models.ForeignKey(
        'home.Usuario',
        on_delete=models.PROTECT,
        related_name='+',
        verbose_name='Usuário de Atualização',
    )
    
    class Meta:
        verbose_name = 'Novo Model'
        verbose_name_plural = 'Novos Models'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            if not self.pk:
                self.usuario_criacao = user
            self.usuario_atualizacao = user
        super().save(*args, **kwargs)
```

### Registrar no __init__.py

```python
# backend/app_name/models/__init__.py
from .novo_model import NovoModel

__all__ = ['NovoModel']
```

---

## 🧪 Testes

### Frontend

```javascript
// frontend/app/components/__tests__/ComponenteNovo.spec.js
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ComponenteNovo from '../ComponenteNovo.vue'

describe('ComponenteNovo', () => {
  it('renderiza corretamente', () => {
    const wrapper = mount(ComponenteNovo, {
      props: {
        item: { label: 'Test' }
      }
    })
    expect(wrapper.text()).toContain('Test')
  })
})
```

### Backend

```python
# backend/app_name/tests/models/test_novo_model.py
from django.test import TestCase
from ...models import NovoModel

class NovoModelTest(TestCase):
    def setUp(self):
        self.model = NovoModel.objects.create(
            nome='Test'
        )
    
    def test_str(self):
        self.assertEqual(str(self.model), 'Test')
    
    def test_ativo_default(self):
        self.assertTrue(self.model.ativo)
```

---

## 🔍 Code Review Checklist

### Frontend

- [ ] Usa componentes do Design System
- [ ] Props bem definidos com types e defaults
- [ ] Responsivo (testado em mobile/tablet/desktop)
- [ ] Sem console.logs desnecessários
- [ ] Imports organizados
- [ ] Nomes descritivos
- [ ] Segue convenções de nomenclatura

### Backend

- [ ] Segue estrutura de pastas padrão
- [ ] Models com verbose_name
- [ ] Admin configurado completamente
- [ ] Permissions corretas no ViewSet
- [ ] Migrations incluídas
- [ ] Testes passando
- [ ] Documentação atualizada

---

## 🚨 Erros Comuns

### ❌ NÃO FAÇA ISSO

#### Frontend

```vue
<!-- ❌ Criando botão do zero -->
<button class="bg-blue-500 px-4 py-2">
  Clique aqui
</button>

<!-- ✅ Use o componente -->
<UiButton tipo="primary" size="md">
  Clique aqui
</UiButton>
```

```javascript
// ❌ Hardcoding valores
const title = 'Título Fixo'

// ✅ Use props
const props = defineProps({
  title: String
})
```

#### Backend

```python
# ❌ Model sem verbose_name
nome = models.CharField(max_length=100)

# ✅ Com verbose_name
nome = models.CharField(
    verbose_name='Nome',
    max_length=100,
)
```

```python
# ❌ Admin sem configuração
admin.site.register(NovoModel)

# ✅ Admin configurado
@admin.register(NovoModel)
class NovoModelAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo', 'data_criacao']
    search_fields = ['nome']
    list_filter = ['ativo']
```

---

## 📚 Recursos Úteis

### Documentação

- [Django Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Nuxt 3 Docs](https://nuxt.com/docs)
- [Quasar Components](https://quasar.dev/vue-components)
- [Tailwind CSS](https://tailwindcss.com/docs)

### Comandos Rápidos

```bash
# Ver componentes disponíveis
ls frontend/app/components/Ui/

# Ver models de um app
ls backend/app_name/models/

# Ver rotas registradas
python backend/manage.py show_urls

# Limpar cache Nuxt
rm -rf frontend/.nuxt frontend/.output

# Resetar banco (cuidado!)
rm backend/db.sqlite3
python backend/manage.py migrate
```

---

## 🤝 Processo de Contribuição

1. **Fork** o repositório (se externo)
2. **Clone** para sua máquina
3. **Crie branch**: `git checkout -b feature/nova-feature`
4. **Desenvolva** seguindo este guia
5. **Teste** localmente
6. **Commit**: `git commit -m "feat: descrição da feature"`
7. **Push**: `git push origin feature/nova-feature`
8. **Pull Request** com descrição detalhada

### Mensagens de Commit

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: adiciona componente de filtro de vagas
fix: corrige bug no upload de currículo
docs: atualiza documentação de setup
style: formata código com prettier
refactor: reorganiza estrutura de pastas
test: adiciona testes para VagaSerializer
chore: atualiza dependências
```

---

## ❓ Dúvidas?

1. Consulte [ARCHITECTURE.md](ARCHITECTURE.md)
2. Veja código similar em apps existentes
3. Use componentes como referência
4. Pergunte no canal do projeto

**Lembre-se**: Consistência é mais importante que perfeição! 🎯
