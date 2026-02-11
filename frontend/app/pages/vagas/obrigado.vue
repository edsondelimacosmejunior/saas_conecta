<template>
  <ClientOnly>
    <main class="grid place-items-center h-screen bg-neutral-20 relative overflow-hidden">
      <DotLottieVue
        class="absolute top-32 mx-auto left-0 right-0"
        style="height: auto; width: 60vw; min-width: 500px;"
        autoplay
        loop
        :src="confetti"
      />
      <q-card
        class="max-w-[30rem] w-full flex flex-col !p-32 gradiente !shadow-none border border-primary-pure/10 overflow-hidden"
      >
        <IcoObrigado class="w-[15rem] mx-auto mt-56" />
        <h1 class="text-title-2 mx-auto text-center mt-32">
          Obrigado{{ query?.nome ? `, ${query.nome}` : '' }}
        </h1>
        <p
          class="max-w-[24rem] mx-auto text-paragraph-1 text-neutral-60 mt-32 tex-center"
        >
          Agradecemos seu interesse na vaga
          {{ query?.vaga ? `de ${query.vaga}.` : '' }}
          Recebemos seu currículo e em breve entraremos em contato.
        </p>
        <UiButton tipo="primary" size="md" class="!w-full mt-32" to="/"
          >Lista de vagas</UiButton
        >
      </q-card>
    </main>
  </ClientOnly>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue'
import confetti from '~/assets/lottie/confetti.lottie'
const query = useRoute().query

useSeoMeta({
  title: `Conecta - Obrigado`,
  robots: { index: false, all: false },
})

</script>

<style lang="scss" scoped>
.gradiente{
  background: linear-gradient(180deg, rgba(17, 210, 118, 0.20) 0%, rgba(17, 210, 118, 0.00) 100%);
}
</style>
