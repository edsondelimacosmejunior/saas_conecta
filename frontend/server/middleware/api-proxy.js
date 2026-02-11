// server/middleware/api-proxy.ts
import {
  defineEventHandler,
  createError,
  readBody,
  readMultipartFormData,
  readFormData,
  getQuery,
} from 'h3'
import { useRuntimeConfig } from '#imports'
import { consola } from 'consola'

const isFormData = (body) => {
  if (body instanceof FormData) {
    return true
  }

  if (typeof body === 'string') {
    return body.includes('multipart/form-data')
  }

  return false
}

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  const url = event.node.req.url
  if (!url || !url.startsWith('/api/')) return
  const apiPath = url
  if (!apiPath) {
    throw createError({
      statusCode: 400,
      statusMessage: 'URL inválida',
    })
  }

  try {
    const targetUrl = `${config.apiUrl}${apiPath}`
    let body
    let headers = { Authorization: `Token ${config.apiSecret}` }
    const method = event.node.req.method
    const query = getQuery(event)
    const requestHeaders = getRequestHeaders(event)
    const contentType = requestHeaders['content-type']

    // if (contentType) headers['Content-Type'] = contentType

    if (method !== 'GET') {
      if (isFormData(contentType)) {
        const formDataBody = await readMultipartFormData(event)
        const formData = new FormData()

        formDataBody?.forEach((value) => {
          if (value.name && value.data) {
            console.log(value.data)

            if (value.name === 'curriculo') {
              const file = new File([value.data], value.filename, {
                type: value.type,
              })
              formData.append(value.name, file)
            } else {
              formData.append(value.name, value.data)
            }
          }
        })
        body = formData
      } else {
        body = await readBody(event)
      }
    }
    console.log(body)

    const response = await $fetch(targetUrl, {
      method,
      body,
      query,
      headers,
    })

    consola.success(`\x1b[32m ${method}\x1b[0m ${targetUrl}`)

    return response
  } catch (error) {
    consola.error(`Erro na requisição: ${error.message}`)
    // console.log(error.data)
    throw createError({
      statusCode: error.statusCode || 500,
      statusMessage: error.message,
      data: error.data,
    })
  }
})
