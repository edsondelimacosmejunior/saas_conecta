import { unref, watch } from 'vue'
import { showError, useRouter, navigateTo } from '#app'

export default function useShowError(error, redirectPath = '/') {
  const router = useRouter()

  const handleError = () => {
    const e = unref(error)
    if (e) {
      // Primeiro, tente redirecionar
      navigateTo(redirectPath).catch(() => {
        // Se o redirecionamento falhar, mostre o erro
        showError({
          statusCode: e?.statusCode || 500,
          statusMessage: e?.statusMessage || 'An error occurred',
          fatal: true,
        })
      })
    }
  }

  // Adiciona o watch dentro do composable
  watch(
    () => unref(error),
    (newError) => {
      if (newError) {
        handleError()
      }
    },
    { immediate: true }
  )

  return handleError
}
