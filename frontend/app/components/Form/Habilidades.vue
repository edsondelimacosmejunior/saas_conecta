<script setup>
/** @typedef {import('../../services/d.types').Vaga} Vaga */
/** @typedef {import('../../services/d.types').VagaRequisitos[]} VagaRequisitos */
/** @typedef {import('../../services/d.types').VagaDifferentials[]} VagaDifferentials */
const props = defineProps({
  vaga: { type: Object, default: () => ({}) },
  requisitos: { type: Array, default: () => [] },
  diferenciais: { type: Object, default: () => ({}) },
})
/** @type {Vaga} */
const vaga = props.vaga
/** @type {VagaRequisitos} */
const requisitos = props.requisitos
/** @type {VagaDifferentials} */
const diferenciais = props.diferenciais
const { vagaForm } = storeToRefs(useVagaFormStore())
const slug = vaga.slug

onMounted(() => {
  requisitos.forEach((requisito) => {
    if (!vagaForm.value[slug]?.requisitos?.[requisito.id]) {
      vagaForm.value[slug].requisitos[requisito.id] = {
        skill: null,
        tempo_experiencia: 0,
      }
    }
  })
})
</script>
<!--

{
  "avaliacao": 0,
  "tempo_experiencia": 0,
  "candidato": 0,
  "skill": 0,
  "usuario_criacao": 0,
  "usuario_atualizacao": 0
}
-->

<template>
  <q-card v-if="requisitos" class="p-32 flex flex-col gap-32">
    <h1 class="orna-verde-left text-headline-1 text-neutral-100 !font-medium">
      Habilidades
    </h1>

    <div class="flex flex-col gap-16 flex-1">
      <template
        v-for="requisito in requisitos"
        :key="'requisito' + requisito.id"
      >
        <div
          class="border border-neutral-100/10 rounded-md px-18 py-12 flex flex-col"
        >
          <p class="text-headline-2 text-neutral-100 mb-24">
            {{ requisito.nome }}
          </p>

          <p class="text-caps-2 text-neutral-60 mb-16">Nível</p>
          <div class="flex items-center gap-32">
            <q-radio
              :model-value="vagaForm[slug]?.requisitos?.[requisito.id]?.skill"
              val="0"
              label="Não possuí"
              size="1.25rem"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].skill = v
                }
              "
            />

            <q-radio
              :model-value="vagaForm[slug]?.requisitos?.[requisito.id]?.skill"
              val="1"
              label="Básico"
              size="1.25rem"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].skill = v
                }
              "
            />
            <q-radio
              :model-value="vagaForm[slug]?.requisitos?.[requisito.id]?.skill"
              val="2"
              label="Intermediário"
              size="1.25rem"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].skill = v
                }
              "
            />
            <q-radio
              :model-value="vagaForm[slug]?.requisitos?.[requisito.id]?.skill"
              val="3"
              label="Avançado"
              size="1.25rem"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].skill = v
                }
              "
            />
            <q-radio
              :model-value="vagaForm[slug]?.requisitos?.[requisito.id]?.skill"
              val="4"
              label="Especialista"
              size="1.25rem"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].skill = v
                }
              "
            />
          </div>
          <div class="flex flex-col">
            <p class="text-caps-2 text-neutral-60 mb-8 mt-24">
              Tempo de Experiência
            </p>
            <q-slider
              :model-value="
                vagaForm[slug]?.requisitos?.[requisito.id]?.tempo_experiencia
              "
              label
              :min="0"
              :max="10"
              color="primary"
              @update:model-value="
                (v) => {
                  vagaForm[slug].requisitos[requisito.id].tempo_experiencia = v
                }
              "
            />
            <div class="flex items-center w-full">
              <span class="text-paragraph-2 text-neutral-60">0+</span>
              <p
                v-if="
                  vagaForm[slug]?.requisitos?.[requisito.id]?.tempo_experiencia
                "
                class="text-headline-3 text-neutral-100 mx-auto flex-1 justify-center text-center"
              >
                Mais do que
                {{
                  vagaForm[slug]?.requisitos?.[requisito.id]?.tempo_experiencia
                }}
                {{
                  vagaForm[slug]?.requisitos?.[requisito.id]
                    ?.tempo_experiencia > 1
                    ? 'anos'
                    : 'ano'
                }}
              </p>
              <span class="text-paragraph-2 text-neutral-60 ml-auto">10+</span>
            </div>
          </div>
        </div>
      </template>
    </div>
  </q-card>
</template>
