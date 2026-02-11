interface RootObject {
  time: number
  blocks: Block[]
  version: string
}

interface Block {
  type: string
  data: Data
}

interface Data {
  text?: string
  style?: string
  items?: string[]
}

function removeHtmlTags(input: string) {
  return input.replace(/<[^>]*>/g, '')
}

const oi = {
  time: 1735413609745,
  blocks: [
    { type: 'List', data: { style: 'unordered', items: ['Vaga', 'vaga'] } },
    {
      type: 'paragraph',
      data: {
        text: '<i>Vaga </i><mark class="cdx-marker">pesada </mark>muito <a href="https://www.google.com">foda </a>que ta <b>osso</b>',
      },
    },
    {
      type: 'paragraph',
      data: {
        text: 'Estamos em busca de um(a) Desenvolvedor(a) Backend Júnior com experiência em PHP e conhecimentos em desenvolvimento de APIs RESTful, bancos de dados relacionais (MySQL, PostgreSQL) e controle de versão com Git. Procuramos alguém com bases sólidas em desenvolvimento web, incluindo boas práticas de performance e segurança. Valorizamos profissionais com atenção aos detalhes, habilidades para solucionar problemas, curiosos(as), proativos(as) e com interesse em crescer no desenvolvimento backend. Você irá participar do desenvolvimento e manutenção de sistemas, colaborando com uma equipe altamente qualificada e contribuindo para a evolução das nossas soluções técnicas. O trabalho será remoto, em horário flexível.',
      },
    },
  ],
  version: '2.18.0',
}
export function editorJS(entrada: string, conf: object = {}) {
  if (!entrada)
    return {
      toHTML: () => '',
      toRaw: () => '',
    }
  const json: RootObject = JSON.parse(entrada)
  const config = {
    class: {
      paragraph: 'text-paragraph-1 text-neutral-100 mt-8 mb-16',
      List: 'text-paragraph-1 text-neutral-100  relative',
      ListCircle:
        'size-8 rounded-full absolute top-8 -left-16  border border-neutral-100/40',
    },
  }
  Object.assign(config, conf)

  const types = (block: Block) => ({
    paragraph: `<p class='${config.class.paragraph}'> ${block.data.text} </p>`,
    List: `
    <ul class='${config.class.List}'>
      ${block.data?.items
        ?.map(
          (item) =>
            `<li class='relative ml-16 mb-8'><span class='${config.class.ListCircle}'></span>${item}</li>`
        )
        ?.join('')}
    </ul>`,
  })

  return {
    toHTML: () =>
      json?.blocks?.map((block) => {
        return types(block)[block.type as keyof typeof types]
      }),
    /** pega o primerio  paragraph e retorna o texto Raw*/
    toRaw: () =>
      removeHtmlTags(
        json.blocks.filter((block) => block.type === 'paragraph')?.[0]?.data
          .text || ''
      ),
  }
}

/** gera meta description com entrada do editorjs */
export const editorJSDescription = (value: string, length = 150) =>
  sliceWithoutCuttingWords(editorJS(value)?.toRaw(), length) || ''
