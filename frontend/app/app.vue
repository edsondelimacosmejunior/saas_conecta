<script setup>
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

useSeoMeta({
  title: 'Conecta - Novadata',
  description: '',
  ogImage: '/og-image.png',
  
})

onMounted(() => {
  gsap.registerPlugin(ScrollTrigger)
  console.log('\x1b[32m.\x1b[37mnovadata\x1b[0m')
  console.log('https://novadata.com.br/')
})
</script>

<template>
  <NuxtLayout>
    <NuxtPage />
  </NuxtLayout>
</template>

<style>
@import "assets/css/cores.sass";
@import "assets/css/quasar/@index.sass";
@import "assets/css/app.sass";
</style>
