<script setup lang="ts">
const { error } = defineProps({
  error: { type: Object, default: () => ({}) },
})

const handleError = () => clearError({ redirect: '/' })
</script>

<template>
  <main class="w-screeb h-screen grid place-items-center">
    <div class="mt-120 ">
      <h2 class="text-title-2">Error</h2>
      <h2>{{ error?.statusCode }}</h2>
      <p>{{ error?.statusMessage }}</p>
      <UiButton size="md" tipo="primary" @click="handleError"
        >Voltar para a página inicial</UiButton
      >
    </div>
  </main>
</template>
