<script setup lang="ts">
const { vaga } = defineProps<{
  vaga: Vaga
}>()
const { data: beneficios } = await useAsyncData(`beneficio-${vaga.id}`, () =>
  vagasService.getVagaBeneficios(vaga?.id)
)

const regimeTrabalho = computed(
  () =>
    TIPO_REGIME_TRABALHO[
      vaga?.tipo_regime_trabalho as keyof typeof TIPO_REGIME_TRABALHO
    ]
)
</script>

<template>
  <q-card class="flex items-center p-24 gap-24 max-lg:gap-16 max-lg:p-16">
    <template v-for="beneficio in beneficios" :key="beneficio.id">
    <UtilFlexCenter class="!flex-nowrap">
        <IcoBeneficio class="size-24 flex-shrink-0" />
        <p class="text-paragraph-2 max-lg:text-paragraph-3 text-neutral-70">
          {{ beneficio.nome }}
        </p>
      </UtilFlexCenter>
    </template>

    <UtilFlexCenter v-if="regimeTrabalho" class="!flex-nowrap">
      <IcoHomeOffice class="size-24 flex-shrink-0" />
      <p class="text-paragraph-2 max-lg:text-paragraph-3 text-neutral-70">
        {{ regimeTrabalho }}
      </p>
    </UtilFlexCenter>

    <UtilFlexCenter v-if="vaga.salario" class="!flex-nowrap">
      <IcoSalario class="size-24 flex-shrink-0" />
      <p class="text-paragraph-2 max-lg:text-paragraph-3 text-neutral-70">
        {{ vaga.salario }}
      </p>
    </UtilFlexCenter>

    <UtilFlexCenter v-if="vaga.tipo_contratacao" class="!flex-nowrap">
      <IcoSalario class="size-24 flex-shrink-0" />
      <p class="text-paragraph-2 max-lg:text-paragraph-3 text-neutral-70">
        {{
          TIPO_CONTRATACAO[
            vaga.tipo_contratacao as keyof typeof TIPO_CONTRATACAO
          ]
        }}
      </p>
    </UtilFlexCenter>
  </q-card>
</template>

<style lang="scss" scoped></style>
