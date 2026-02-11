export const candidatosService = {
  /** @typedef {import { CandidatoPost } from "./d.types.ts";} CandidatoPost */
  /** @typedef {import { PostFormacaoCandidato } from "./d.types.ts";} PostFormacaoCandidato */
  /** @typedef {import { PostSkillsCandidato } from "./d.types.ts";} PostSkillsCandidato */
  /** @typedef {import { PostRespostasAbertas } from "./d.types.ts";} PostRespostasAbertas */
  /** @typedef {import { PostVerificarEmail } from "./d.types.ts";} PostVerificarEmail */

  /**
   * @param {CandidatoPost} body
   */
  async postCandidato(body) {
    console.log('postCandidato')
    return await $fetch('/api/candidatos/', {
      method: 'POST',
      body,
    })
  },

  /**
   * @param {PostFormacaoCandidato} body
   */
  async postFormacaoCandidato(body) {
    return await $fetch('/api/formacoes-candidatos/', {
      method: 'POST',
      body,
    })
  },
  /**
   * @param {PostSkillsCandidato} body
   */
  async postSkillsCandidato(body) {
    return await $fetch('/api/skills-candidatos/', {
      method: 'POST',
      body,
    })
  },
  /**
   * @param {PostRespostasAbertas} body
   */
  async postPerguntaAdicional(body) {
    return await $fetch('/api/respostas-abertas/', {
      method: 'POST',
      body,
    })
  },
  /**
   * @param {PostVerificarEmail} body
   */
  async postVerificarEmail(body) {
    return await $fetch(`/api/candidatos/verificar-email/`, {
      method: 'POST',
      body,
    })
  },
}
