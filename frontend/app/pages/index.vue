<script setup>
import { date } from 'quasar'

const { data, error } = useAsyncData(`vagas`, () => vagasService.getVagas())
const { data: areasAtuacao } = useAsyncData(`areasAtuacao`, () =>
  vagasService.getAreasAtuacao()
)

const vagas = computed(
  () => data.value?.results?.sort(ordenateKey('data_criacao'))?.reverse() || []
)

// if (!vagas.value?.length) navigateTo('error')

const areasAtuacaoVagas = computed(
  () =>
    areasAtuacao.value?.results?.filter((area) => {
      return vagas.value.find((vaga) => vaga.area_atuacao === area.id)
    }) || []
)

const areasFilter = ref([])
const search = ref('')

const vagasFiltered = computed(() => {
  return vagas.value.map((vaga) => {
    // Verifica se a busca está preenchida e se o título corresponde
    const matchesSearch =
      !search.value ||
      vaga.titulo.toLowerCase().includes(search.value.toLowerCase())

    // Verifica se a área selecionada corresponde
    const matchesArea =
      areasFilter.value.length === 0 ||
      areasFilter.value.includes(vaga.area_atuacao)

    // O item será incluído apenas se ambos os critérios forem atendidos
    return {
      ...vaga,
      hidden: !(matchesSearch && matchesArea),
    }
  })
})
function onBtnFilterClick(id) {
  if (areasFilter.value?.find((area) => id === area))
    areasFilter.value = areasFilter.value.filter((v) => v !== id)
  else areasFilter.value.push(id)
}
</script>

<template>
  <q-scroll-area class="bg-neutral-30 h-full">
    <section class="container-md !mt-32 !pt-56">
      <header
        class="p-24 bg-primary-pure/10 mb-16 rounded-md border border-primary-pure/20 max-lg:!p-16"
      >
        <h2 class="text-title-2 max-lg:text-title-3 mb-4">
          Construa Sua Carreira com a Novadata
        </h2>
        <p class="text text-paragraph-2 text-neutral-70">
          Junte-se à nossa equipe e faça parte da transformação digital com
          metodologias inovadoras e ferramentas personalizadas.
        </p>
        <UiInput
          v-model="search"
          placeholder="Busque pela vaga..."
          class="w-full bg-white mt-32 no-label"
          size="md"
        >
          <template #prepend>
            <q-icon class="text-neutral-60" name="search"></q-icon> </template
        ></UiInput>

        <Suspense>
          <div class="flex items-center gap-10 mt-16">
            <UiButton
              class="bg-white"
              :class="{ primary: areasFilter.length === 0 }"
              @click="areasFilter = []"
              tipo="secondary"
              size="md"
              label="Tudo"
            />

            <template v-for="area in areasAtuacaoVagas" :key="area.id">
              <UiButton
                tipo="secondary"
                size="md"
                class="bg-white !text-neutral-60"
                :class="{ primary: areasFilter.includes(area.id) }"
                @click="onBtnFilterClick(area.id)"
                >{{ area.nome }}</UiButton
              >
            </template>
          </div>
        </Suspense>
        <p v-if="vagasFiltered.filter((v) => !v.hidden && v.ativa).length" class="text-paragraph-2 text-neutral-70 mt-18">
          {{ vagasFiltered.filter((v) => !v.hidden && v.ativa).length }}
          vagas abertas
        </p>
      </header>
      <div class="flex flex-col gap-16 mb-56">
        <div class="flex flex-col gap-16">
          <q-item
            v-for="vaga in vagasFiltered"
            :key="vaga.id"
            v-show="vaga.ativa"
            :class="{ hidden: vaga.hidden }"
            class="border border-neutral-100/10 rounded flex flex-col bg-white !p-24 !pb-0 max-lg:!px-16 max-lg:!pt-16"
          >
            <div class="flex flex-col">
              <div
                class="flex w-full !flex-nowrap mb-8 max-lg:flex-col-reverse gap-8 max-lg:gap-10"
              >
                <h1 class="text-title-2 max-lg:!text-title-3 text-neutral-100">
                  {{ vaga.titulo }}
                </h1>
                <div
                  class="flex flex-col gap-4 ml-auto shrink-0 max-lg:flex-row-reverse max-lg:m-0 max-lg:justify-between max-lg:items-center max-sm:!flex-nowrap max-sm:!gap-0"
                >
                  <q-badge
                    class="py-6 !rounded-xl w-max px-10"
                    :class="{
                      '!bg-neutral-100/5 !text-neutral-100': !vaga.ativa,
                      '!bg-primary-pure-dark/5 !text-primary-pure-dark':
                        vaga.ativa,
                    }"
                    :label="
                      vaga.ativa ? 'Candidatura Aberta' : 'Candidatura Fechada'
                    "
                  />
                  <span class="text-paragraph-3 text-neutral-100/40 max-lg:ml-0"
                    >Publicado em:
                    {{ date.formatDate(vaga.data_criacao, 'DD MMM') }}</span
                  >
                </div>
              </div>
              <p class="text-neutral-70 text-paragraph-2">
                {{ editorJSDescription(vaga.sobre, 190) }}...
              </p>
            </div>
            <VagaAttributes :vaga class="!border-0 !shadow-none !p-0 mt-24" />
            <div
              class="border h-1 w-auto border-dashed -mx-32 border-neutral-30 mt-24"
            ></div>
            <NuxtLink
              v-if="vaga.ativa"
              v-ripple="{ early: true, color: 'blue-grey-3' }"
              class="py-24 transition-colors -mx-24 group relative hover:bg-neutral-20"
              :to="`/vagas/${vaga.slug}`"
              ><div class="flex items-center gap-4 px-24">
                <p
                  class="text-underline-dashed text-headline-3 !font-medium text-neutral-100"
                >
                  Ver detalhes e candidatar-se
                </p>
                <IcoArrowRight
                  class="size-18 transition-transform group-hover:translate-x-6"
                /></div
            ></NuxtLink>
          </q-item>
          <ClientOnly>
            <UiEmpty
              text="Nada encontrado"
              class="mt-32"
              v-if="vagasFiltered.filter((vaga) => !vaga?.hidden)?.length === 0"
            />
          </ClientOnly>
        </div>
      </div>
    </section>
  </q-scroll-area>
</template>

<style lang="sass" scoped>
.primary
  background: rgb(var(--primary-pure)) !important
  color: rgb(var(--neutral-100)) !important
</style>
