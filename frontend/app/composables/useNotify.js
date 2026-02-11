import { Notify } from 'quasar'

export default function () {

  return {
    notifySucess(message, opt = {}) {
      Notify.create({
        color: 'primary',
        message,
        position: 'top',
        ...opt,
      })
    },
    notifyError(message, opt = {}) {
      Notify.create({
        color: 'red',
        message,
        position: 'top',
        ...opt,
      })
    },
  }
}
