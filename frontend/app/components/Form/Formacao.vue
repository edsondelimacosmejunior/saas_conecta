<script setup>
import { date } from 'quasar'

const $q = useQuasar()
/** @typedef {import('../../services/d.types').Vaga} Vaga */
/** @typedef {import('../../services/d.types').CandidatoPost} Vaga */
const props = defineProps({
  /** @type {Vaga} */
  vaga: { type: Object, default: () => ({}) },
})

/** @type {Vaga} */
const vaga = props.vaga

const { vagaForm } = storeToRefs(useVagaFormStore())

const slug = vaga.slug
/** @type {{value: CandidatoPost}} */
const vagaActive = computed(() => vagaForm.value[slug])
const modelCurrent = ref({})
// interface FormacaoCandidatoPost {
//   grau: number;
//   data_inicio: string;
//   data_conclusao: string;
//   candidato: number;
//   instituicao: string;
//   curso: string;
//   usuario_criacao: number;
//   usuario_atualizacao: number;
// }
// onMounted(() => {
//   if (!vagaActive.value.formacao) vagaForm.value[slug].formacao = []
// })

const valid = computed(() => {
  const { curso, data_conclusao, instituicao, grau, data_inicio } = modelCurrent.value
  return [curso, data_conclusao, instituicao, grau, data_inicio].every((v) => v)
})

function addFormacao() {
  if (!valid.value) {
    $q.notify({
      color: 'red',
      message: 'Preencha todos os campos para adicionar uma formação',
      position: 'top',
    })
    return
  }
  vagaForm.value[slug].formacao = [
    ...vagaActive.value.formacao,
    modelCurrent.value,
  ]
  modelCurrent.value = {}
}
</script>

<template>
  <q-card class="p-32">
    <h1
      class="orna-verde-left text-headline-1 text-neutral-100 !font-medium mb-32"
    >
      Formações
    </h1>
    <template v-if="vagaActive.formacao?.length">
      <div class="flex flex-col gap-8">
        <div
          v-for="(formacao, i) in vagaActive.formacao"
          :key="i"
          class="flex flex-col flex-nowrap gap-4"
        >
          <q-card
            class="relative py-12 px-18 !shadow-none border-neutral-100/10 border flex flex-col flex-nowrap gap-4 group"
          >
            <q-item
              clickable
              class="opacity-0 group-hover:opacity-100 group hover:!bg-alert-error-10 !min-h-0 !p-0 !size-24 absolute -right-8 -top-8 rounded-full !grid place-items-center border border-neutral-100/10 bg-white"
              @click="vagaActive.formacao.splice(i, 1)"
              ><q-icon
                class="group-hover:text-alert-error -mt-3"
                name="close"
              ></q-icon
            ></q-item>

            <p class="text-headline-2 text-neutral-100">
              {{ formacao.curso.nome }}
            </p>
            <p class="text-paragraph-2 text-neutral-70">
              {{
                date.formatDate(
                  formacao.data_conclusao?.replaceAll('-', '/'),
                  'MMM/YYYY'
                )
              }}
            </p>
            <p class="text-paragraph-2 text-neutral-70">
              {{ formacao.instituicao.nome }}
            </p>
            <p class="text-paragraph-2 text-neutral-70">
              {{
                ESCOLARIDADE_GRAU.find(({ value }) => value === formacao.grau)
                  ?.label
              }}
            </p>
          </q-card>
        </div>
      </div>
    </template>

    <div class="grid grid-cols-2 gap-24 mt-32 max-lg:flex max-lg:flex-col">
      <UiLabelWrapper :required="false" text="Nome do Curso">
        <UiSelectedPaginated
          v-model="modelCurrent.curso"
          api-url="/api/cursos/"
          class="bg-neutral-10 no-label"
        />
      </UiLabelWrapper>
      <UiLabelWrapper :required="false" text="Data de Inicio">
        <UiInput
          v-model="modelCurrent.data_inicio"
          type="date"
          placeholder="dd/mm/aaaa"
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper :required="false" text="Data de Conclusão">
        <UiInput
          v-model="modelCurrent.data_conclusao"
          type="date"
          placeholder="dd/mm/aaaa"
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper  :required="false" text="Ensino">
        <UiSelect
          v-model="modelCurrent.grau"
          :options="ESCOLARIDADE_GRAU"
          class="bg-neutral-10"
          use-input
          size="md"
        ></UiSelect>
      </UiLabelWrapper>
      <UiLabelWrapper class="col-span-2"  :required="false" text="Instituição">
      <UiSelectedPaginated
          class="bg-neutral-10 no-label"
          v-model="modelCurrent.instituicao"
          api-url="/api/instituicoes/"
        />
      </UiLabelWrapper>

      <div
        class="border h-1 w-auto border-dashed -mx-32 col-span-2 border-neutral-30 mt-8 mb-8 max-lg:mx-0"
      ></div>
      <div class="flex w-full col-span-2">
        <UiButton
          :disable="!valid"
          tipo="secondary"
          size="md"
          class="!px-24 w-full flex-1 !h-48"
          @click="addFormacao"
          ><q-icon name="add" class="!text-neutral-100/50 !size-16"></q-icon
          >Adicionar Formação</UiButton
        >
      </div>
    </div>
  </q-card>
</template>
