export default function (error) {
  const { notifyError } = useNotify()

  if (
    typeof error?.data === 'string' ||
    typeof error?.data?.data === 'string'
  ) {
    notifyError(
      'Ocorreu um erro inesperado no servidor. Tente novamente mais tarde.'
    )
    return
  }

  if (error?.data?.data) {
    Object.entries(error.data.data).forEach(([key, value]) => {
      notifyError(`${key}: ${Array.isArray(value) ? value.join(', ') : value}`)
    })
  } else if (error?.data) {
    Object.entries(error.data).forEach(([key, value]) => {
      notifyError(`${key}: ${Array.isArray(value) ? value.join(', ') : value}`)
    })
  } else {
    notifyError('Ocorreu um erro inesperado. Tente novamente.')
  }
}
