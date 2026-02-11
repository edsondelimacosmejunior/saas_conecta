<script setup>
defineProps({
  text: {
    type: String,
    default: '',
  },
  required: {
    type: Boolean,
    default: true,
  },
})
</script>
<template>
  <label class="flex flex-col gap-4">
    <p class="text-headline-3" :class="{ 'w-max required': required }">
      {{ text }}
    </p>
    <slot></slot>
  </label>
</template>
