# Design System - Componentes Disponíveis

## 🎨 Componentes Base (Ui/)

### UiButton

Botão padrão do sistema.

**Localização**: `frontend/app/components/Ui/UiButton.vue`

**Props**:
```typescript
{
  tipo: 'primary' | 'secondary' | 'tertiary'  // Estilo do botão
  size: 'sm' | 'md' | 'lg'                    // Tamanho
  label: string                                // Texto do botão
  disabled: boolean                            // Estado desabilitado
  loading: boolean                             // Estado de carregamento
}
```

**Uso**:
```vue
<UiButton tipo="primary" size="md" @click="handleClick">
  Salvar
</UiButton>
```

---

### UiInput

Input de formulário padrão.

**Localização**: `frontend/app/components/Ui/UiInput.vue`

**Props**:
```typescript
{
  modelValue: any                // v-model binding
  placeholder: string            // Placeholder
  size: 'sm' | 'md' | 'lg'      // Tamanho
  type: string                   // Tipo HTML (text, email, etc)
  disabled: boolean              // Estado desabilitado
  error: string                  // Mensagem de erro
}
```

**Slots**:
- `prepend`: Ícone/conteúdo antes do input
- `append`: Ícone/conteúdo depois do input

**Uso**:
```vue
<UiInput
  v-model="search"
  placeholder="Busque pela vaga..."
  size="md"
>
  <template #prepend>
    <q-icon name="search" />
  </template>
</UiInput>
```

---

### UiEmpty

Estado vazio para listas/conteúdos.

**Localização**: `frontend/app/components/Ui/UiEmpty.vue`

**Props**:
```typescript
{
  text: string     // Texto a exibir
  icon: string     // Ícone (opcional)
}
```

**Uso**:
```vue
<UiEmpty
  v-if="items.length === 0"
  text="Nenhum item encontrado"
/>
```

---

## 🧩 Componentes de Feature

### Vaga Components

Localização: `frontend/app/components/Vaga/`

#### VagaCard
Card de vaga para listagens.

**Props**:
- `vaga: Object` - Objeto da vaga

#### VagaAttributes
Atributos da vaga (salário, tipo, regime).

**Props**:
- `vaga: Object` - Objeto da vaga

#### VagaDescription
Descrição completa da vaga.

**Props**:
- `vaga: Object` - Objeto da vaga

#### VagaResponsabilities
Responsabilidades da vaga.

**Props**:
- `vaga: Object` - Objeto da vaga

#### VagaDifferentials
Diferenciais da vaga.

**Props**:
- `vaga: Object` - Objeto da vaga

---

## 🎯 Quasar Components

O projeto usa Quasar UI Framework. Componentes disponíveis:

### Layout & Navigation
- `q-scroll-area` - Área com scroll customizado
- `q-item` - Item de lista
- `q-badge` - Badge/etiqueta

### Form Components
- `q-input` - Input (use `UiInput` quando possível)
- `q-select` - Select/dropdown
- `q-checkbox` - Checkbox
- `q-radio` - Radio button

### Display
- `q-icon` - Ícones
- `q-img` - Imagens otimizadas
- `q-avatar` - Avatar circular

**Documentação**: https://quasar.dev/vue-components

---

## 🎨 Tailwind Classes

Use classes utilitárias do Tailwind para estilização:

### Cores (Sistema Customizado)
```scss
// Usando RGB vars
bg-primary-pure         // Cor primária
text-neutral-100        // Texto escuro
text-neutral-70         // Texto médio
bg-neutral-20           // Background claro
```

### Responsividade
```scss
max-lg:text-sm         // Em telas ≤ lg
max-sm:hidden          // Em telas ≤ sm
```

### Spacing
```scss
p-24      // padding 24px
mt-32     // margin-top 32px
gap-16    // gap 16px
```

---

## 📖 Como Criar Novo Componente

### 1. Verifique se já existe!

```bash
# Liste componentes existentes
ls frontend/app/components/Ui/
ls frontend/app/components/[Feature]/
```

### 2. Template de Componente

```vue
<!-- frontend/app/components/Ui/UiNovoComponente.vue -->
<script setup>
/**
 * Descrição curta do componente
 * 
 * @component UiNovoComponente
 * @example
 * <UiNovoComponente
 *   :items="myItems"
 *   variant="primary"
 *   @select="handleSelect"
 * />
 */

// Props com validação
const props = defineProps({
  items: {
    type: Array,
    default: () => []
  },
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary'].includes(value)
  }
})

// Emits documentados
const emit = defineEmits([
  'select',  // Quando item é selecionado
  'change'   // Quando valor muda
])

// Computed e lógica
const hasItems = computed(() => props.items.length > 0)

// Métodos
const handleClick = (item) => {
  emit('select', item)
}
</script>

<template>
  <div class="novo-componente" :class="`variant-${variant}`">
    <!-- Use componentes existentes -->
    <UiButton
      v-for="item in items"
      :key="item.id"
      @click="handleClick(item)"
    >
      {{ item.label }}
    </UiButton>
    
    <!-- Estado vazio -->
    <UiEmpty v-if="!hasItems" text="Nenhum item disponível" />
  </div>
</template>

<style scoped>
/* Evite estilos. Use Tailwind quando possível */
.novo-componente {
  /* Apenas se absolutamente necessário */
}
</style>
```

### 3. Checklist

- [ ] Props com tipos e defaults
- [ ] Emits documentados
- [ ] Usa componentes existentes
- [ ] Usa Tailwind (evita CSS customizado)
- [ ] Responsivo (testado em mobile/tablet)
- [ ] JSDoc com exemplo de uso
- [ ] Nome descritivo (PascalCase)

---

## 🔄 Composables Úteis

### useAsyncData
Nuxt built-in para fetch de dados com cache.

```vue
<script setup>
const { data, error, pending } = await useAsyncData(
  'chave-unica',
  () => servicoAPI.getData()
)
</script>
```

### useShowError
Customizado para exibir erros.

```vue
<script setup>
const { data, error } = await useAsyncData(/* ... */)
useShowError(error)
</script>
```

### useRoute / useRouter
Nuxt built-ins para roteamento.

```vue
<script setup>
const route = useRoute()
const router = useRouter()

const id = route.params.id
router.push('/vagas')
</script>
```

---

## 🎯 Services

### vagasService

**Localização**: `frontend/app/services/vagas.service.js`

**Métodos**:
```javascript
// Buscar vaga por slug
vagasService.getVaga(slug)

// Buscar todas as vagas
vagasService.getVagas()

// Benefícios da vaga
vagasService.getVagaBeneficios(id)

// Requisitos da vaga
vagasService.getVagaRequisitos(id)

// Diferenciais da vaga
vagasService.getVagaDiferenciais(id)

// Perguntas adicionais
vagasService.getVagaPerguntasAdicionais(id)

// Áreas de atuação
vagasService.getAreasAtuacao()
```

**Uso**:
```vue
<script setup>
const { data } = await useAsyncData(
  'vaga-123',
  () => vagasService.getVaga('backend-jr')
)
</script>
```

---

## 🚀 Boas Práticas

### ✅ FAÇA

```vue
<!-- ✅ Reutilize componentes -->
<UiButton tipo="primary">Salvar</UiButton>

<!-- ✅ Use props -->
<VagaCard :vaga="item" />

<!-- ✅ Tailwind para responsividade -->
<div class="flex flex-col gap-16 max-lg:gap-8">

<!-- ✅ Composables para lógica compartilhada -->
const { data } = useAsyncData()
```

### ❌ NÃO FAÇA

```vue
<!-- ❌ Criar UI do zero -->
<button class="custom-button">Clique</button>

<!-- ❌ Hardcode -->
<h1>Título Fixo</h1>

<!-- ❌ CSS inline -->
<div style="margin-top: 20px">

<!-- ❌ Lógica duplicada -->
// Mesma lógica em vários componentes
```

---

## 📱 Responsividade

### Breakpoints Tailwind

```scss
sm: 640px   // max-sm:  ≤ 640px
md: 768px   // max-md:  ≤ 768px
lg: 1024px  // max-lg:  ≤ 1024px
xl: 1280px  // max-xl:  ≤ 1280px
```

### Exemplo Responsivo

```vue
<template>
  <div class="
    flex flex-col gap-16
    lg:flex-row lg:gap-24
    max-sm:gap-8
  ">
    <h1 class="
      text-title-2
      max-lg:text-title-3
      max-sm:text-paragraph-1
    ">
      Título Responsivo
    </h1>
  </div>
</template>
```

---

## 🔍 Debug

### Vue DevTools

Use Vue DevTools para inspecionar componentes, props e state.

### Console Úteis

```javascript
// Ver dados computados
console.log('Vagas:', vagas.value)

// Ver props
console.log('Props:', props)

// Ver reactive state
console.log('State:', toRaw(state))
```

---

## 📚 Referências

- [Componentes Quasar](https://quasar.dev/vue-components)
- [Tailwind Docs](https://tailwindcss.com/docs)
- [Nuxt Components](https://nuxt.com/docs/guide/directory-structure/components)
- [Vue 3 Composition API](https://vuejs.org/guide/extras/composition-api-faq.html)

---

**Dúvidas?** Veja componentes similares já implementados no projeto!
