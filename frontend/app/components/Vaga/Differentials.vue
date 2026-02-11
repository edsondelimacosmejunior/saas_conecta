<script setup lang="ts">
const { vaga } = defineProps<{
  vaga: Vaga
}>()
const { data: diferenciais } = await useAsyncData(
  `diferencial-${vaga.id}`,
  () => vagasService.getVagaDiferenciais(vaga?.id)
)
</script>

<template>
  <template v-if="diferenciais?.filter((dif) => dif.descricao)?.length">
    <div
      class="border h-1 w-auto border-dashed -mx-32 border-neutral-30 mt-32 mb-32 max-lg:mx-0"
    ></div>
    <p class="text-caps-2 text-neutral-60 mb-12">Diferenciais</p>

    <div class="text-paragraph-1 text-neutral-100 relative">
      <template v-for="diferencial in diferenciais">
        <p
          v-if="diferencial.descricao"
          :key="diferencial.id"
          class="relative ml-16 mb-8"
        >
          <span
            class="size-8 rounded-full absolute top-8 -left-16 border border-neutral-100/40"
          ></span>
          {{ diferencial.descricao }}
        </p>
      </template>
    </div>
  </template>
</template>

<style scoped></style>
