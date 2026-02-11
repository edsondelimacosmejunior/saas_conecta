<script setup>
import { useMediaQuery } from '@vueuse/core'

const isLargeScreen = useMediaQuery('(min-width: 1280px)')

const props = defineProps({ text: String })
</script>

<template>
  <q-item
    id="vaga-detail"
    :style="{
      boxShadow: '0px 1px 1px 0px rgba(0, 0, 0, 0.06)',
      left: isLargeScreen ? 'calc(50% + 400px - 16px)' : null,
    }"
    clickable
    tipo="secondary"
    class="bg-white !p-32 max-lg:!p-16 flex-col border border-neutral-100/10 rounded-md group w-[250px] max-xl:w-full fixed max-xl:!relative top-[5.5rem] max-xl:top-0"
  >
    <div class="flex flex-col">
      <IcoTitle class="size-24 mb-16" />
      <p class="text-headline-2">{{ text }}</p>
      <div class="flex items-center gap-4 mt-16">
        <p
          class="text-underline-dashed text-headline-3 !font-medium text-neutral-100"
        >
          Ver detalhes
        </p>
        <IcoArrowRight
          class="size-18 transition-transform group-hover:translate-x-6"
        />
      </div>
    </div>
  </q-item>
</template>

<style lang="scss" scoped></style>
