<script setup lang="ts">
const { vaga } = defineProps<{
  vaga: Vaga
}>()

// const editor = editorJS
const sobreHTML = computed(() => editorJS(vaga.responsabilidades).toHTML())
</script>

<template>
  <template v-if="vaga.responsabilidades">
    <div
      class="border h-1 w-auto border-dashed -mx-32 border-neutral-30 mt-32 mb-32 max-lg:mx-0"
    />
    <template v-if="vaga.responsabilidades">
      <p class="text-caps-2 text-neutral-60 mb-12">Responsabilidades</p>
      <template v-for="(text, i) in sobreHTML" :key="i">
        <div v-html="text"></div>
      </template>
    </template>
  </template>
</template>

<style scoped></style>
