<script setup>
const headerStore = useHeaderStore()
</script>

<template>
  <header
    class="bg-white flex h-56 p-12 items-center border-b border-b-neutral-100/10 fixed top-0 left-0 w-full z-50"
  >
    <NuxtLink to="/"
      ><IcoLogoLight
        class="w-[12.6875rem] h-32 absolute top-0 bottom-0 my-auto left-64 max-2xl:left-24"
    /></NuxtLink>
    <div class="container-md">
      <div class="max-xl:!hidden">
        <p class="text-caps-2 text-neutral-60 !font-normal">
          {{ headerStore.header.text }}
        </p>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped></style>
