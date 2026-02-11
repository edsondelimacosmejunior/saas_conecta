// stores/user.ts
import { defineStore, acceptHMRUpdate } from 'pinia'

export const useVagaFormStore = defineStore(
  'vagaForm',
  () => {
    const vagaForm = ref({})
    const curriculos = ref({})

    return {
      vagaForm,
      curriculos,
    }
  },
  {
    persist: {
      omit: ['curriculos'],
    },

    skipHydration: true,
  }
)
if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useVagaFormStore, import.meta.hot))
}
