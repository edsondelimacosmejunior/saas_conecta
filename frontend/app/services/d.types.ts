export interface Vaga {
  id: number
  titulo: string
  slug: string
  sobre: string
  ativa: boolean
  responsabilidades: string
  data_fechamento: string
  salario: string
  tipo_contratacao: string
  vaga_generica: boolean
  tipo_regime_trabalho: string
  data_criacao: string
  data_atualizacao: string
  area_atuacao: number
  usuario_criacao: number
  usuario_atualizacao: number
  beneficios: number[]
  requisitos: number[]
  diferenciais: number[]
}

export interface VagaBeneficios {
  id: number
  nome: string
  descricao: string
  data_criacao: string
  data_atualizacao: string
  usuario_criacao: number
  usuario_atualizacao: number
}
export interface VagaDifferentials {
  id: number
  nome: string
  tipo: string
  descricao: string
  data_criacao: string
  data_atualizacao: string
  usuario_criacao: number
  usuario_atualizacao: number
}
export interface VagaRequisitos {
  id: number
  nome: string
  tipo: string
  descricao: string
  data_criacao: string
  data_atualizacao: string
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface PaginatedResponse<T> {
  count: number
  next: string | null
  previous: string | null
  results: T[]
}

export type PaginatedVaga = PaginatedResponse<Vaga>

export interface CandidatoPost {
  formacao_candidato: Formacaocandidato[]
  skill_candidato: Skillcandidato[]
  resposta_aberta: Respostaaberta[]
  nome: string
  sobre_mim: string
  email: string
  whatsapp: string
  data_nascimento: string
  estado: string
  expectativa_2anos: string
  expectativa_10anos: string
  resposta_vaga_generica: string
  comunicativo: boolean
  ingles: number
  empregado: boolean
  disponibilidade: string
  horarios: string
  pretensao_salarial_pj: string
  pretensao_salarial_clt: string
  curriculo: string
  github_portfolio: string
  linkedin: string
  indicacao: string
  vaga: number
  usuario_criacao: number
  usuario_atualizacao: number
}

interface Respostaaberta {
  resposta: string
  candidato: number
  pergunta_aberta: number
  usuario_criacao: number
  usuario_atualizacao: number
}

interface Skillcandidato {
  avaliacao: number
  tempo_experiencia: number
  candidato: number
  skill: number
  usuario_criacao: number
  usuario_atualizacao: number
}

interface Formacaocandidato {
  grau: number
  data_inicio: string
  data_conclusao: string
  candidato: number
  instituicao: number
  curso: number
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface Candidato {
  id: number
  nome: string
  sobre_mim: string
  email: string
  whatsapp: string
  data_nascimento: string
  estado: string
  expectativa_2anos: string
  expectativa_10anos: string
  resposta_vaga_generica: string
  comunicativo: boolean
  ingles: number
  empregado: boolean
  disponibilidade: string
  horarios: string
  pretensao_salarial_pj: string
  pretensao_salarial_clt: string
  curriculo: string
  github_portfolio: string
  linkedin: string
  indicacao: string
  data_criacao: string
  data_atualizacao: string
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface PostFormacaoCandidato {
  grau: number
  data_inicio: string
  data_conclusao: string
  candidato: number
  instituicao: number
  curso: number
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface PostSkillsCandidato {
  avaliacao: number
  tempo_experiencia: number
  candidato: number
  skill: number
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface PostRespostasAbertas {
  resposta: string
  candidato: number
  pergunta_aberta: number
  usuario_criacao: number
  usuario_atualizacao: number
}
export interface PerguntasAdicionais {
  id: number
  titulo: string
  obrigatorio: boolean
  data_criacao: string
  data_atualizacao: string
  vaga: number
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface AreaAtuacao {
  id: number
  nome: string
  descricao: string
  data_criacao: string
  data_atualizacao: string
  usuario_criacao: number
  usuario_atualizacao: number
}

export interface PostVerificarEmail {
  vaga_id: number
  email: string
}

export interface InputEmailStatus {
  loading: boolean,
  message: string,
  valid: boolean
}
