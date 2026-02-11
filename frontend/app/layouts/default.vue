<script setup>
import img from 'public/logo.png'

</script>

<template>
  <q-layout view="hHh Lpr fFf">
    <HeaderBase />
    <q-page-container class="h-screen overflow-y-auto">
      <slot></slot>
    </q-page-container>
    <img
      class="fixed bottom-16 right-16"
      :src="img"
      alt="logo conecta simbola verde e texto preto"
    />
  </q-layout>
</template>
