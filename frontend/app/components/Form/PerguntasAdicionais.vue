<script setup>
/** @typedef {import('../../services/d.types').PerguntasAdicionais[]} PerguntasAdicionais */
const props = defineProps({
  vaga: { type: Object, default: () => ({}) },
  perguntasAdicionais: { type: Array, default: () => [] },
})

/** @type {Vaga} */
const vaga = props.vaga
const { vagaForm } = storeToRefs(useVagaFormStore())
const slug = vaga.slug
/** @type {PerguntasAdicionais} */
const perguntasAdicionais = props.perguntasAdicionais

onMounted(() => {
  perguntasAdicionais?.forEach((pergunta) => {
    if (!vagaForm.value[slug]?.perguntasAdicionais?.[pergunta.id]) {
      vagaForm.value[slug].perguntasAdicionais[pergunta.id] = {
        resposta: '',
      }
    }
  })
})
</script>

<template>
  <q-card class="p-32" v-if="perguntasAdicionais.length">
    <h1
      class="orna-verde-left text-headline-1 text-neutral-100 !font-medium mb-32"
    >
      Perguntas Adicionais
    </h1>
    <div class="flex flex-col gap-24 ">
      <UiLabelWrapper
        :required="false"
        v-for="pergunta in perguntasAdicionais"
        :key="pergunta.id"
        :text="pergunta.titulo"
        class="col-span-2 "
      >
        <UiInput
          :model-value="
            vagaForm[slug]?.perguntasAdicionais?.[pergunta.id]?.resposta || ''
          "
          :rules="[requiredValidation]"
          autogrow
          placeholder="Digite aqui..."
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
          @update:model-value="
            (v) => {
              vagaForm[slug].perguntasAdicionais[pergunta.id].resposta = v
            }
          "
        >
        </UiInput>
      </UiLabelWrapper>
    </div>
  </q-card>
</template>
