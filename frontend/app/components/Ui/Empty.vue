<template>
  <div
    class="text-paragraph-2 text-center m-auto !h-full flex-1 flex flex-col justify-center"
  >
  <div class="mx-auto my-16">
    <IcoEmptyDesert class="h-auto w-[160px] " />

  </div>
    <p class="opacity-40 mb-8" :class="classP">{{ text }}</p>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: 'Nada aqui.',
  },
  classP: String,
})

const icons = ['fluorescent', 'spa', 'light']

function getRandomIndex(array) {
  const randomIndex = Math.floor(Math.random() * array.length)
  return randomIndex
}
</script>

<style lang="scss" scoped></style>
