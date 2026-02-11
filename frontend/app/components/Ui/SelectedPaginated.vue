<script setup>
const props = defineProps({
  apiUrl: {
    type: String,
    required: true,
  },
  // /** Id para diferenciar as requisicoes */
  // selectID: {
  //   type: String,
  //   required: true,
  // },

  label: {
    type: String,
    default: null,
  },
  optionValue: {
    type: String,
    default: 'id',
  },
  optionLabel: {
    type: String,
    default: 'nome',
  },
  inputDebounce: {
    type: Number,
    default: 300,
  },
  queryParam: {
    type: String,
    default: 'search',
  },
  limitParam: {
    type: String,
    default: 'page_size',
  },

  initialLimit: {
    type: Number,
    default: 25,
  },
})

const urlDefault = `${props.apiUrl}?${props.limitParam}=${props.initialLimit}`

const options = ref([])
const loading = ref(false)
const nextUrl = ref(urlDefault)

const stringOptions = ref([]) // Opcões carregadas localmente

// Filter function (local + async)
const searchOld = ref(null)
const filterFn = async (val, update, abort) => {
  if (!val && !searchOld.value) return update()
  const deletedText = !val && searchOld.value

  if (deletedText) {
    console.log('filterFn deletedText')
    searchOld.value = null
    nextUrl.value = urlDefault
    resetOptions()
    fetchInitialOptions()
    return update()
  }

  // Debounce na busca para evitar requisições excessivas
  if (loading.value) {
    abort()
    return
  }
  searchOld.value = val
  nextUrl.value = ''
  loading.value = true
  try {
    const url = new URL(props.apiUrl, window.location.origin) // Garante URL válida
    url.searchParams.set(props.queryParam, val) // Adiciona o parâmetro de busca
    url.searchParams.set(props.limitParam, props.initialLimit) // Limite de resultados por página

    const response = await $fetch(url.toString())
    const results = response?.results || []

    options.value = results // Atualiza as opções com os resultados da busca
    update(() => {})
  } catch (error) {
    console.error('Erro na busca:', error)
  } finally {
    loading.value = false
  }
}

const fetchInitialOptions = async (query) => {
  if (loading.value) return
  loading.value = true
  try {
    /* prettier-ignore */
    const nextUrl = `${props.apiUrl}?${props.queryParam}=${query || ''}&${props.limitParam}=${props.initialLimit}`
    const request = await $fetch(nextUrl)
    const results = request.results || []

    // Se houver resultados, atualiza as opções
    if (results?.length > 0) {
      options.value = results
      stringOptions.value = [...stringOptions.value, ...results] // Armazena para filtro local
    }
  } catch (error) {
    console.error('Erro ao buscar dados:', error)
  } finally {
    loading.value = false
  }
}

const loadMore = async () => {
  if (!nextUrl.value || loading.value) return

  loading.value = true
  try {
    const req = await $fetch(nextUrl.value)

    if (req.results && req.results.length > 0) {
      options.value = [...options.value, ...req.results]
    }

    if (req.next) {
      const url = new URL(req.next)
      const { origin } = url
      nextUrl.value = req.next.replace(origin, '')
    } else {
      nextUrl.value = undefined
    }
  } catch (error) {
    console.error('Erro ao buscar dados:', error)
  } finally {
    loading.value = false
  }
}

const resetOptions = () => {
  options.value = []
  stringOptions.value = []
}

const initializeOptions = async () => {
  resetOptions()
  nextUrl.value = `${props.apiUrl}?${props.limitParam}=${props.initialLimit}`
  fetchInitialOptions()
}

onMounted(() => {
  initializeOptions()
})

const handleVirtualScroll = (details) => {
  if (details.index < props.initialLimit - 1) return
  const scrollToLastItem =
    details.to >= options.value.length - 1 && !loading.value
  if (scrollToLastItem) loadMore()
}
</script>

<template>
  <q-select
    class="bg-neutral-10 size-md label-transparent"
    dropdown-icon="expand_more"
    clear-icon="clear"
    :fill-input="false"
    :input-debounce="inputDebounce"
    :options="options"
    :loading="loading"
    @virtual-scroll="handleVirtualScroll"
    @focus="initializeOptions"
    @filter="filterFn"
    use-input
    map-options
    :option-value="optionValue"
    :option-label="optionLabel"
    :label="label"
    :model-value="null"
    @update:model-value="initializeOptions"
  >
    <template #no-option>
      <div v-if="!loading" class="!my-26">
        <ui-empty />
      </div>
    </template>
  </q-select>
</template>
