<script setup>
/** @typedef {import('quasar').QInput} Props */
/** @type {Props} */
defineProps({})
defineOptions({ inheritAttrs: false })
const componentRef = ref(null)

const slots = useSlots()
const attrs = useAttrs()

defineExpose({ componentRef })
</script>

<template>
  <q-input
    v-bind="attrs"
    ref="componentRef"
    class="o-input"
    :class="'size-' + attrs.size"
    :size="null"
  >
    <template v-for="slot in Object.keys(slots)" #[slot]>
      <slot :name="slot"></slot>
    </template>
  </q-input>
</template>

<style lang="sass">
.body--dark
  .o-input
    input:-webkit-autofill
        -webkit-box-shadow: 0 0 0px 100px rgb(var(--d-neutral-30)) inset
        -webkit-text-fill-color: rgba(var(--white), 0.9) !important

    input:-webkit-autofill:focus
      -webkit-box-shadow: 0 0 0 100px rgb(var(--d-neutral-30)) inset
      -webkit-text-fill-color: rgba(var(--white), 0.9) !important

.body--light
  .o-input
    input:-webkit-autofill
        -webkit-box-shadow: 0 0 0px 500px rgb(var(--white)) inset
        -webkit-text-fill-color: rgba(var(--neutral-70), 1) !important

    input:-webkit-autofill:focus
      -webkit-box-shadow: 0 0 0 50px rgb(var(--white)) inset
      -webkit-text-fill-color: rgba(var(--neutral-70), 1) !important
</style>
