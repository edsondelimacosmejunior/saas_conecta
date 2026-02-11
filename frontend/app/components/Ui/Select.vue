<script></script>

<script setup>
import { useSlots, useAttrs, ref, onMounted, watch, nextTick } from 'vue'
/** @typedef {import('./types').UiSelectProps} Props */
/** @type {Props} */
const props = defineProps({})
const val = ref('')
const slots = useSlots()
const attrs = useAttrs()
const componentRef = ref(null)
const options = ref(attrs.options)

let stringOptions = attrs.options
defineOptions({
  inheritAttrs: false,
})
// function handleFocus() {
//   componentRef.value.showPopup()
// }
// asas
watch(
  () => attrs.options,
  async (v) => {
    await nextTick()
    options.value = attrs.options
    stringOptions = attrs.options
  },
  { deep: true }
)

function filterFn(val, update, abort) {
  update(() => {
    if (!val) return (options.value = stringOptions)
    const needle = val?.toLowerCase()
    options.value = stringOptions.filter((v) => {
      const option = v[attrs['option-label'] || 'label']
      const have = option?.toLowerCase().indexOf(needle) > -1
      return have
    })
  })
}

defineExpose({ componentRef })
</script>

<template>
  <q-select
    ref="componentRef"
    emit-value
    map-options
    class="Oselect bg-neutral-10"
    :class="'size-' + attrs.size"
    popup-content-class="select-menu"
    input-debounce="300"
    transition-duration="150"
    options-selected-class="option-selecionada"
    v-bind="attrs"
    :size="null"
    :options="options"
    dropdown-icon="expand_more"
    clear-icon="clear"
    @filter="filterFn"
  >
    <template v-for="slot in Object.keys(slots)" #[slot]="slotProps">
      <slot :name="slot" v-bind="slotProps"></slot>
    </template>

    <template #no-option>
      <q-item>
        <div class="flex items-center gap-8">
          <q-icon
            class="block mx-auto opacity-30"
            name="fluorescent"
            size="2rem"
          ></q-icon>
          <p class="opacity-40">Sem Dados para exibir.</p>
        </div></q-item
      >
    </template>
  </q-select>
</template>

<style lang="sass">
.q-select--multiple
  .q-field__native
    gap: 2px
    padding: 4px 2px 2px

.q-select--single
  .q-field__native
    flex-wrap: nowrap
    span
      flex: 0 3 auto
    input
      flex: 1
</style>
