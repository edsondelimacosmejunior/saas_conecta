const isMobile = () => window.matchMedia('(max-width:1024px)').matches

function createFormData(obj) {
  const formData = new FormData()
  for (const key in obj) {
    if (obj.hasOwnProperty(key)) {
      formData.append(key, obj[key])
    }
  }
  return formData
}

const testPattern = {
  url: (v) => /^(https?:\/\/)([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(\/.*)?$/.test(v),
  email: (v) =>
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
      v
    ),
  tel: (v) => /^\(?\d{2}\)?\s?(?:9\d{4}|\d{4})-?\d{4}/.test(v),
  date: (v) => /^(19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$/.test(v),
}

const requiredValidation = (val) => {
  if (val === null || val === undefined || val === '') {
    return 'Este campo é obrigatório'
  }
  return true
}

function scrollToFocusedElement() {
  const focusedElement = document.activeElement
  if (focusedElement) {
    focusedElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
  }
}

/**
 * Creates an object composed of the picked `object` properties.
 * @param {object} obj The source object.
 * @param {array} keys The property names to pick
 * @returns Returns the new object.
 * @example
 * var object = { 'a': 1, 'b': '2', 'c': 3 };
 * pick(object, ['a', 'c']);
 * // => { 'a': 1, 'c': 3 }
 */
function pick(obj, keys) {
  return keys.reduce((result, key) => {
    if (key in obj) result[key] = obj[key]
    return result
  }, {})
}

function realToNumber(v) {
  const centavos = `${v}`.startsWith('0.')
  const value = parseFloat(`${v}`.replace(/\./g, '').replace(',', '.'))
  return centavos ? Number(`0.${value}`) : value
}

const ordenateKey = (key) => (a, b /* sort cb */) => {
  if (a[key] > b[key]) return 1
  if (a[key] < b[key]) return -1
  return 0
}

export {
  isMobile,
  createFormData,
  testPattern,
  scrollToFocusedElement,
  requiredValidation,
  pick,
  realToNumber,
  ordenateKey,
}
