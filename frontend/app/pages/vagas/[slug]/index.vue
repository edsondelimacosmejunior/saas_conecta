<script setup>
const slug = useRoute().params?.slug
const { data, error } = await useAsyncData(`vaga-${slug}`, () =>
  vagasService.getVaga(slug)
)
const vaga = computed(() => data.value.results.at())
useShowError(error)
if (!vaga.value) navigateTo('error')

useSeoMeta({
  title: vaga.value.titulo,
  description: editorJSDescription(vaga.value.sobre),
})
</script>

<template>
  <q-scroll-area class="bg-neutral-20 h-full">
    <section class="container-md !mt-32 !pt-56">
      <div class="flex items-center gap-16 mb-16">
        <IcoTitle class="size-32 transparent" />
        <h1 class="text-title-2 text-neutral-100 !font-medium">
          {{ vaga.titulo }}
        </h1>
      </div>

      <VagaAttributes :vaga />

      <VagaDescription :vaga class="mt-12 mb-64 flex flex-col">
        <VagaResponsabilities :vaga />
        <VagaDifferentials :vaga />
        <NuxtLink v-if="vaga.ativa" :to="`/vagas/${slug}/form`">
          <UiButton
            class="!w-full flex-1 mt-24"
            tipo="primary"
            size="md"
          >
            Candidatar-se</UiButton
          ></NuxtLink
        >
        <p v-else class="text-neutral-70 text-paragraph-1  mt-32 h-48 flex justify-center cursor-not-allowed items-center text-center rounded-md bg-neutral-100/10 w-full">Candidatura Expirada</p>
      </VagaDescription>
    </section>
  </q-scroll-area>
</template>

<style lang="scss" scoped></style>
