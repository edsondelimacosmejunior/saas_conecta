<script setup lang="ts">
const { vaga } = defineProps<{
  vaga: Vaga
}>()

const { data: beneficios } = await useAsyncData(`beneficio-${vaga.id}`, () =>
  vagasService.getVagaBeneficios(vaga?.id)
)

// const editor = editorJS
const sobreHTML = computed(() => editorJS(vaga.sobre).toHTML())
</script>

<template>
  <QCard class="p-32">
    <template v-if="vaga.sobre">
      <p class="text-caps-2 text-neutral-60 mb-12">Sobre a vaga</p>
      <template v-for="(text, i) in sobreHTML" :key="i">
        <div v-html="text"></div>
      </template>
    </template>
    <slot></slot>
  </QCard>
</template>

<style scoped></style>
