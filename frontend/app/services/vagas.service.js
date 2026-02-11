export const vagasService = {
  /** @typedef {import { Vaga } from "./d.types.ts";} PaginatedVaga */
  /** @typedef {import { VagaBeneficios } from "./d.types.ts";} VagaBeneficios */
  /** @typedef {import { VagaDifferentials } from "./d.types.ts";} VagaDifferentials */
  /** @typedef {import { AreaAtuacao } from "./d.types.ts";} AreaAtuacao */

  /**
   * @param {string} slug - O slug da vaga
   * @returns {Promise<PaginatedVaga>}
   */
  async getVaga(slug) {
    return await $fetch(`/api/vagas/?slug=${slug}`)
  },

  /**
   * @param {number} id - O slug da vaga
   * @returns {Promise<VagaBeneficios[]>}
   */
  async getVagaBeneficios(id) {
    return await $fetch(`/api/vagas/${id}/beneficios/`)
  },

  /**
   * @param {number} id - O slug da vaga
   * @returns {Promise<VagaDifferentials[]>}
   */
  async getVagaDiferenciais(id) {
    return await $fetch(`/api/vagas/${id}/diferenciais/`)
  },
  /**
   * @param {number} id - O slug da vaga
   * @returns {Promise<VagaRequisitos[]>}
   */
  async getVagaRequisitos(id) {
    return await $fetch(`/api/vagas/${id}/requisitos/`)
  },

  /*   async getVagaPerguntasAdicionais(id) {
    return await $fetch(`/api/vagas/${id}/requisitos`)
  },
 */
  /**
   * @param {number} id - O id da vaga
   */
  async getVagaPerguntasAdicionais(idVaga) {
    return await $fetch(`/api/vagas/${idVaga}/perguntas_adicionais/`)
  },

  /**
   * Busca todas as vagas
   * @returns {Promise<PaginatedVaga>}
   */
  async getVagas() {
    let allResults = []
    let nextPage = '/api/vagas/?page_size=20'

    while (nextPage) {
      const response = await $fetch(nextPage)
      allResults = [...allResults, ...response.results]
      nextPage = response.next
        ? response.next.replace(/^https?:\/\/[^\/]+/, '')
        : null
    }
    return {
      results: allResults,
      count: allResults.length,
    }
  },

  /**
   * Busca todas as vagas
   * @returns {Promise<AreaAtuacao>}
   */
  async getAreasAtuacao() {
    return await $fetch('/api/areas-atuacoes/')
  },
}
