// stores/user.ts
import { defineStore } from 'pinia'

export const useHeaderStore = defineStore('header', () => {
  const header = ref({
    text: '',
  })

  return {
    header,
  }
})
