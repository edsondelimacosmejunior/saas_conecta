<script setup>
/** @typedef {import('../../services/d.types').Vaga} Vaga */
/** @typedef {import('../../services/d.types').VagaDifferentials[]} VagaDifferentials */
const props = defineProps({
  vaga: { type: Object, default: () => ({}) },
  diferenciais: { type: Object, default: () => ({}) },
})

/** @type {Vaga} */
const vaga = props.vaga
const { slug } = vaga

/** @type {VagaDifferentials} */
const diferenciais = props.diferenciais

const { vagaForm } = storeToRefs(useVagaFormStore())

onMounted(() => {
  if (!vagaForm.value[slug]?.diferenciais) {
    vagaForm.value[slug].diferenciais = []
  }

  if (!vagaForm.value[slug]?.interesse_diferenciais) {
    vagaForm.value[slug].interesse_diferenciais = []
  }
})
</script>

<template>
  <q-card class="p-32">
    <h1 class="orna-verde-left text-headline-1 text-neutral-100 !font-medium">
      Diferenciais
    </h1>

    <p class="text-paragraph-2 text-neutral-60 mt-4">
      Selecione os diferenciais que você possui:
    </p>

    <div class="my-32 flex flex-col gap-32">
      <q-checkbox
        v-for="(diferencial, _index) in diferenciais"
        :key="diferencial.id"
        v-model="vagaForm[slug].diferenciais"
        :label="diferencial.nome"
        :val="diferencial.id"
        size="24px"
      />
    </div>

    <UiLabelWrapper
      :required="false"
      text="Explique brevemente seu interesse ou contato com os diferenciais escolhidos (opcional):"
    >
      <UiInput
        :model-value="vagaForm[slug].interesse_diferenciais"
        autogrow
        placeholder="Digite aqui..."
        class="bg-neutral-10 no-label"
        input-class="!min-h-40 !pt-12"
        size="md"
        @update:model-value="
          (v) => {
            vagaForm[slug].interesse_diferenciais = v
          }
        "
      >
      </UiInput>
    </UiLabelWrapper>
  </q-card>
</template>
