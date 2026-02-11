<script setup>
import { QBtn } from 'quasar'

defineOptions({
  inheritAttrs: false,
})
/** @typedef {import('./types').UiButtonProps} Props */
/** @type {Props} */
const props = defineProps({})
const slots = useSlots()
const attrs = useAttrs()

const padding = {
  sm: '.5rem .375rem',
  md: '.5rem .5625rem',
  lg: '.5rem  .75rem',
}

const sizes = { sm: '.75rem ', md: '.875rem', lg: '1rem' }
const height = { sm: '2rem ', md: '2.5rem', lg: '3rem' }

const iconSize = computed(() =>
  attrs['icon-size'] ? attrs['icon-size'] : '1.715em'
)

const setPadding = padding[attrs.size]
const setSize = sizes[attrs.size]
const setHeight = height[attrs.size]
</script>

<template>
  <q-btn
    v-bind="attrs"
    :ripple="{ early: true }"
    :padding="setPadding"
    :size="setSize"
    :style="{ minHeight: setHeight }"
  >
    <template v-for="slot in Object.keys(slots)" #[slot]>
      <slot :name="slot" />
    </template>
  </q-btn>
</template>

<style lang="sass">
.q-btn
    --icon-size: v-bind(iconSize)

    .q-icon
      font-size: var(--icon-size, 1.715em) !important
</style>
