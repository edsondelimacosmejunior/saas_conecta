const TIPO_REGIME_TRABALHO = {
  PRESENCIAL: 'Presencial',
  HIBRIDO: 'Híbrido',
  HOME_OFFICE: 'Home Office',
}

const TIPO_CONTRATACAO = {
  CLT: 'CLT',
  PJ: 'PJ',
  ESTAGIO: 'Estágio',
  FREELANCER: 'Freelancer',
}

const ESTADOS = [
  { label: 'Acre', value: 'AC' },
  { label: 'Alagoas', value: 'AL' },
  { label: 'Amapá', value: 'AP' },
  { label: 'Amazonas', value: 'AM' },
  { label: 'Bahia', value: 'BA' },
  { label: 'Ceará', value: 'CE' },
  { label: 'Distrito Federal', value: 'DF' },
  { label: 'Espírito Santo', value: 'ES' },
  { label: 'Goiás', value: 'GO' },
  { label: 'Maranhão', value: 'MA' },
  { label: 'Mato Grosso', value: 'MT' },
  { label: 'Mato Grosso do Sul', value: 'MS' },
  { label: 'Minas Gerais', value: 'MG' },
  { label: 'Pará', value: 'PA' },
  { label: 'Paraíba', value: 'PB' },
  { label: 'Paraná', value: 'PR' },
  { label: 'Pernambuco', value: 'PE' },
  { label: 'Piauí', value: 'PI' },
  { label: 'Rio De Janeiro', value: 'RJ' },
  { label: 'Rio Grande do Norte', value: 'RN' },
  { label: 'Rio Grande do Sul', value: 'RS' },
  { label: 'Rondônia', value: 'RO' },
  { label: 'Roraima', value: 'RR' },
  { label: 'Santa Catarina', value: 'SC' },
  { label: 'São Paulo', value: 'SP' },
  { label: 'Sergipe', value: 'SE' },
  { label: 'Tocantins', value: 'TO' },
]
const INGLES_NIVEL = [
  { label: 'Não tem', value: 0 },
  { label: 'Básico', value: 1 },
  { label: 'Intermediário', value: 2 },
  { label: 'Avançado', value: 3 },
  { label: 'Fluente', value: 4 },
]
const DISPONIBILIDADE = [
  { label: 'Imediata', value: 'IMEDIATA' },
  { label: '30 dias', value: '30DIAS' },
  { label: '60 dias', value: '60DIAS' },
  { label: '90 dias', value: '90DIAS' },
  { label: '120 dias', value: '120DIAS' },
]
const HORARIOS_DISPONIBILIDADE = [
  { label: 'Part-time', value: 'PART-TIME' },
  { label: 'Full-time', value: 'FULL-TIME' },
]
const ESCOLARIDADE_GRAU = [
  { value: 1, label: 'Técnico Incompleto' },
  { value: 2, label: 'Técnico' },
  { value: 3, label: 'Graduação Incompleta' },
  { value: 4, label: 'Graduação' },
  { value: 5, label: 'Pós-Graduação Incompleta' },
  { value: 6, label: 'Pós-Graduação' },
  { value: 7, label: 'Mestrado Incompleto' },
  { value: 8, label: 'Mestrado' },
  { value: 9, label: 'Doutorado Incompleto' },
  { value: 10, label: 'Doutorado' },
]

const CANDIDATO_FIELDS = [
  'nome',
  'sobre_mim',
  'email',
  'whatsapp',
  'data_nascimento',
  'estado',
  'expectativa_2anos',
  'expectativa_10anos',
  'resposta_vaga_generica',
  'comunicativo',
  'ingles',
  'empregado',
  'disponibilidade',
  'horarios',
  'pretensao_salarial_pj',
  'pretensao_salarial_clt',
  'curriculo',
  'github_portfolio',
  'indicacao',
  'linkedin',
  'linkedin',
]
export {
  TIPO_REGIME_TRABALHO,
  TIPO_CONTRATACAO,
  ESTADOS,
  INGLES_NIVEL,
  DISPONIBILIDADE,
  HORARIOS_DISPONIBILIDADE,
  ESCOLARIDADE_GRAU,
  CANDIDATO_FIELDS,
}
