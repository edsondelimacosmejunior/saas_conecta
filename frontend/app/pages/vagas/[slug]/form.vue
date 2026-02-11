<script setup>
import ModalVagaDetail from '~/components/Modal/VagaDetail.vue'
import ModalTermos from '~/components/Modal/Termos.vue'
import { Dialog, scroll } from 'quasar'

const slug = useRoute().params?.slug

const { data, error } = await useAsyncData(`vaga-${slug}`, () =>
  vagasService.getVaga(slug)
)
const vaga = computed(() => data.value.results.at())

const { data: perguntasAdicionais } = await useAsyncData(
  `pergunta-adicional-${slug}`,
  () => vagasService.getVagaPerguntasAdicionais(vaga.value.id)
  // { transform: (v) => v?.results }
)
const { data: requisitos } = await useAsyncData(`requisitos-${slug}`, () =>
  vagasService.getVagaRequisitos(vaga.value.id)
)
const { data: diferenciais } = await useAsyncData(
  `diferencial-${vaga.value.id}`,
  () => vagasService.getVagaDiferenciais(vaga.value?.id)
)

useShowError(error)

const intialValue = {
  vagaID: vaga.value.id,
  formacao: [],
  termos: false,
  requisitos: {},
  diferenciais: [],
  perguntasAdicionais: {},
}

if (!vaga.value) navigateTo('error')
if (!vaga.value.ativa) navigateTo('/')

const { header } = storeToRefs(useHeaderStore())
const { vagaForm, curriculos } = storeToRefs(useVagaFormStore())

const vagaActive = computed(() => vagaForm.value[slug])

function openModalVagaDetail() {
  Dialog.create({
    component: ModalVagaDetail,
    componentProps: { vaga: vaga.value },
  })
}

function openModalTermos() {
  Dialog.create({ component: ModalTermos })
}

async function clearFields(reload = true) {
  vagaForm.value[slug] = intialValue
  curriculos.value = {}
  await nextTick()
  reload && window.location.reload()
}
const formRef = ref(null)
const scrollAreaRef = ref(null)
const loading = ref(false)
const { notifyError, notifySucess } = useNotify()

async function onSubmit(evt) {
  loading.value = true
  const valid = document.querySelector('#form-vaga').checkValidity()
  const qValid = await formRef.value.validate(true)

  if (!valid || !qValid) {
    scrollToFocusedElement()
    notifyError('Campos Invalidos')
    loading.value = false
    return
  } else await sendForm()

  loading.value = false
}

async function sendForm() {
  const fields = vagaForm.value[slug]
  const body = pick(fields, CANDIDATO_FIELDS)

  try {
    const formData = createFormData({
      ...body,
      pretensao_salarial_clt: realToNumber(body.pretensao_salarial_clt),
      pretensao_salarial_pj: realToNumber(body.pretensao_salarial_pj),
      vaga: vaga.value.id,
    })

    formData.append('curriculo', curriculos.value[slug])
    formData.append(
      'formacao_candidato',
      JSON.stringify(
        fields.formacao.map((formacao) => ({
          curso: formacao.curso.id,
          instituicao: formacao.instituicao.id,
          grau: formacao.grau,
          data_conclusao: formacao.data_conclusao,
          data_inicio: formacao.data_inicio,
        }))
      )
    )
    formData.append(
      'skill_candidato',
      JSON.stringify(
        Object.entries(fields.requisitos)?.map(([id, value]) => ({
          skill: +id,
          tempo_experiencia: value.tempo_experiencia || 0,
          avaliacao: +value.skill || 0,
        }))
      )
    )

    formData.append('interesse_diferenciais', fields.interesse_diferenciais)

    formData.append(
      'resposta_diferencial',
      JSON.stringify(
        fields.diferenciais.map((id) => ({
          skill: id,
          resposta: true,
        }))
      )
    )

    formData.append(
      'resposta_aberta',
      JSON.stringify(
        Object.entries(fields.perguntasAdicionais).map(([id, value]) => ({
          pergunta_aberta: +id,
          resposta: value.resposta,
        }))
      )
    )

    const candidato = await candidatosService.postCandidato(formData)
    const nome = fields.nome
    clearFields(false)
    setTimeout(() => {
      navigateTo(`/vagas/obrigado/?nome=${nome}&vaga=${vaga.value.titulo}`, {
        replace: true,
      })
    }, 100)
  } catch (error) {
    useApiError(error)
  } finally {
    loading.value = false
  }
}

const inputEmailStatus = ref({
  loading: false,
  message: null,
  valid: null,
})

async function onVerifyEmail(email) {
  if (!testPattern.email(email)) return

  try {
    inputEmailStatus.value.loading = true

    const body = {
      vaga_id: vaga.value.id,
      email: email,
    }

    // Verifica se o email já foi usado para se candidatar a essa vaga
    const resposta = await candidatosService.postVerificarEmail(body)
    inputEmailStatus.value.valid = !resposta.exists
    inputEmailStatus.value.message = resposta.message
  } catch (error) {
    useApiError(error)
    inputEmailStatus.value.valid = false
    inputEmailStatus.value.message = 'Erro ao verificar email'
  } finally {
    inputEmailStatus.value.loading = false
  }
}

onMounted(async () => {
  await nextTick()
  if (!vagaForm.value?.[slug]) vagaForm.value[slug] = intialValue
  header.value.text = 'Preencha o formulário'
  document.querySelector('input')?.focus()
})

onUnmounted(() => {
  header.value.text = ''
})

useSeoMeta({
  title: `Conecta - Formulario - ${vaga.value.titulo}`,
  robots: { index: false, all: false },
})
</script>

<template>
  <q-scroll-area class="bg-neutral-20 h-full" ref="scrollAreaRef">
    <q-form
      greedy
      v-if="vagaForm?.[slug]"
      id="form-vaga"
      ref="formRef"
      class="container-md !mt-32 relative !pt-56 !pb-56 flex flex-col gap-16 flex-nowrap"
    >
      <VagaButtonOpen
        :text="vaga.titulo"
        class="max-lg:-order-1"
        @click="openModalVagaDetail"
      />

      <FormDadosCadastrais
        :vaga
        :input-email-status
        @input:verify-email="onVerifyEmail"
      />
      <FormFormacao :vaga />
      <FormHabilidades :vaga :requisitos :diferenciais />
      <FormDiferenciais v-if="diferenciais.length" :vaga :diferenciais />
      <FormPerguntasAdicionais :vaga :perguntas-adicionais />
      <!-- Termos -->
      <section>
        <label
          class="flex !flex-nowrap gap-4 !items-start cursor-pointer select-none"
        >
          <q-field
            lazy-rules
            :rules="[(val) => val || '']"
            :model-value="vagaForm[slug].termos"
            borderless
            :bottom-slots="false"
            :hide-bottom-space="true"
          >
            <q-checkbox
              v-model="vagaForm[slug].termos"
              size="18px"
              class="mt-2"
            />
          </q-field>
          <p class="text-headline-3 text-neutral-70">
            Declaro que li e concordo com os
            <strong
              class="text-underline-dashed text-neutral-100 hover:text-primary-pure"
              @click.stop.prevent="openModalTermos"
              >Termos e Condições</strong
            >
            e autorizo o uso dos meus dados para fins relacionados a este
            processo seletivo.
          </p>
        </label>

        <div class="flex w-full justify-between mt-16">
          <UiButton
            tipo="secondary"
            size="md"
            class="!min-w-[100px] bg-white"
            @click="clearFields"
          >
            Limpar formulário
          </UiButton>
          <UiButton
            :loading
            tipo="primary"
            size="md"
            class="!min-w-[100px]"
            @click="onSubmit"
            >Enviar</UiButton
          >
        </div>
      </section>
    </q-form>
    <ClientOnly>
      <Teleport to="body">
        <q-inner-loading :showing="loading">
          <div class="flex flex-col gap-2">
            <q-spinner-puff size="50px" color="primary" />
            <p>Enviando...</p>
          </div>
        </q-inner-loading>
      </Teleport>
    </ClientOnly>
  </q-scroll-area>
</template>

<style lang="scss" scoped></style>
