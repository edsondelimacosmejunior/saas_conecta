<script setup>
/** @typedef {import('../../services/d.types').Vaga} Vaga */
/** @typedef {import('../../services/d.types').CandidatoPost} Vaga */
/** @typedef {import('../../services/d.types').InputEmailStatus} InputEmailStatus */

const props = defineProps({
  vaga: { type: Object, default: () => ({}) },
  inputEmailStatus: { type: Object, default: () => ({}) },
})

/** @type {Vaga} */
const vaga = props.vaga

/** @type {InputEmailStatus} */
const inputEmailStatus = props.inputEmailStatus

const { vagaForm, curriculos } = storeToRefs(useVagaFormStore())

const slug = vaga.slug
/** @type {CandidatoPost} */
// const vagaActive = computed(() => vagaForm.value[slug])
const options = [
  { label: 'Sim', value: 'true' },
  { label: 'Não', value: 'false' },
]

defineEmits(['input:verify-email'])
</script>

<template>
  <q-card class="p-32">
    <h1 class="orna-verde-left text-headline-1 text-neutral-100 !font-medium">
      Dados Cadastrais
    </h1>
    <div class="grid grid-cols-2 gap-24 mt-32 max-lg:flex-col max-lg:flex">
      <UiLabelWrapper text="Nome">
        <UiInput
          v-model="vagaForm[slug].nome"
          :rules="[requiredValidation]"
          name="name"
          placeholder="Digite seu nome"
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Email">
        <UiInput
          v-model="vagaForm[slug].email"
          :rules="[
            (v) => testPattern.email(v) || 'Email invalido',
            () => inputEmailStatus.valid || inputEmailStatus.message
          ]"
          type="email"
          name="email"
          placeholder="email@email.com"
          class="bg-neutral-10 no-label"
          size="md"
          debounce="300"
          :loading="inputEmailStatus.loading"
          @update:model-value="$emit('input:verify-email', vagaForm[slug].email)"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Whatsapp">
        <UiInput
          v-model="vagaForm[slug].whatsapp"
          :rules="[(v) => testPattern.tel(v) || 'Numero Invalido']"
          type="tel"
          name="telefone"
          placeholder="Ex.: (11) 91234-5678"
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Data de Nascimento">
        <UiInput
          v-model="vagaForm[slug].data_nascimento"
          :rules="[(v) => testPattern.date(v) || 'Data Invalida']"
          name="birthdate"
          type="date"
          placeholder="dd/mm/aaaa"
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Estado">
        <UiSelect
          v-model="vagaForm[slug].estado"
          use-input
          :rules="[requiredValidation]"
          size="md"
          name="state"
          :options="ESTADOS"
          placeholder="Selecione seu estado"
        ></UiSelect>
      </UiLabelWrapper>
      <UiLabelWrapper text="Inglês">
        <UiSelect
          v-model="vagaForm[slug].ingles"
          use-input
          :rules="[requiredValidation]"
          size="md"
          name="state"
          :options="INGLES_NIVEL"
          placeholder="Selecione seu nível"
        ></UiSelect>
      </UiLabelWrapper>
      <UiLabelWrapper text="Disponibilidade">
        <UiSelect
          v-model="vagaForm[slug].disponibilidade"
          use-input
          size="md"
          name="state"
          :rules="[requiredValidation]"
          :options="DISPONIBILIDADE"
          placeholder="Selecione sua disponibilidade"
        ></UiSelect>
      </UiLabelWrapper>
      <UiLabelWrapper text="Horários">
        <UiSelect
          v-model="vagaForm[slug].horarios"
          :rules="[requiredValidation]"
          use-input
          size="md"
          name="state"
          :options="HORARIOS_DISPONIBILIDADE"
          placeholder="Selecione seu horário disponível"
        ></UiSelect>
      </UiLabelWrapper>

      <UiLabelWrapper text="Comunicativo">
        <div class="flex items-center gap-32 mt-16">
          <q-field
            lazy-rules
            class="hide-bottom-slot ![--input-size:1.5rem]"
            :rules="[(val) => !!val || 'Campo obrigatório']"
            :model-value="vagaForm[slug].comunicativo"
            borderless
            :bottom-slots="false"
          >
            <q-option-group
              v-model="vagaForm[slug].comunicativo"
              :options="options"
              size="1.25rem"
              inline
            />
          </q-field>
        </div>
      </UiLabelWrapper>

      <UiLabelWrapper text="Empregado">
        <div class="flex items-center gap-32 mt-16">
          <q-field
            required
            lazy-rules
            class="hide-bottom-slot ![--input-size:1.5rem]"
            :rules="[(val) => !!val || 'Campo obrigatório']"
            :model-value="vagaForm[slug].empregado"
            borderless
            :bottom-slots="false"
          >
            <q-option-group
              v-model="vagaForm[slug].empregado"
              :options="options"
              size="1.25rem"
              inline
            >
              <template #error> <div>-</div> </template></q-option-group
            >
          </q-field>
        </div>
      </UiLabelWrapper>

      <UiLabelWrapper text="Pretensão Salarial CLT">
        <UiInput
          v-model="vagaForm[slug].pretensao_salarial_clt"
          :rules="[requiredValidation]"
          type="text"
          prefix="R$"
          placeholder="0,00"
          mask="###.###.###.###,##"
          reverse-fill-mask
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>

      <UiLabelWrapper text="Pretensão Salarial PJ">
        <UiInput
          v-model="vagaForm[slug].pretensao_salarial_pj"
          :rules="[requiredValidation]"
          type="text"
          prefix="R$"
          placeholder="0,00"
          mask="###.###.###.###,##"
          reverse-fill-mask
          class="bg-neutral-10 no-label"
          size="md"
        ></UiInput>
      </UiLabelWrapper>

      <UiLabelWrapper :required="false" text="Github">
        <UiInput
          v-model="vagaForm[slug].github_portfolio"
          name="github"
          :rules="[(v) => (!v ? true : testPattern.url(v) || 'URL Invalida')]"
          type="text"
          placeholder="github.com/usuario"
          class="bg-neutral-10 no-label"
          size="md"
        >
          <template #prepend>
            <q-icon class="text-neutral-100/40" name="link" />
          </template>
        </UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Linkedin">
        <UiInput
          v-model="vagaForm[slug].linkedin"
          required
          :rules="[(v) => testPattern.url(v) || 'URL Invalida']"
          type="text"
          placeholder="linkedin.com/in/usuario"
          class="bg-neutral-10 no-label"
          size="md"
        >
          <template #prepend>
            <q-icon class="text-neutral-100/40" name="link" />
          </template>
        </UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Quem indicou você para esta vaga?" :required="false" class="col-span-2">
        <UiInput
          v-model="vagaForm[slug].indicacao"
          autogrow
          placeholder="Digite o nome completo do colaborador"
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
        ></UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Sobre mim" class="col-span-2">
        <UiInput
          v-model="vagaForm[slug].sobre_mim"
          :rules="[requiredValidation]"
          autogrow
          placeholder="Ex.: Sou apaixonado por tecnologia, com experiência em desenvolvimento de software..."
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
        >
        </UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Como se enxerga em 2 anos?" class="col-span-2">
        <UiInput
          v-model="vagaForm[slug].expectativa_2anos"
          :rules="[requiredValidation]"
          autogrow
          placeholder="Ex.: Quero estar trabalhando como desenvolvedor pleno, ampliando meus conhecimentos..."
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
        >
        </UiInput>
      </UiLabelWrapper>
      <UiLabelWrapper text="Como se enxerga em 10 anos?" class="col-span-2">
        <UiInput
          v-model="vagaForm[slug].expectativa_10anos"
          :rules="[requiredValidation]"
          autogrow
          placeholder="Ex.: Espero estar liderando equipes de tecnologia e contribuindo para projetos de impacto global."
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
        >
        </UiInput>
      </UiLabelWrapper>

      <UiLabelWrapper text="Currículo" class="col-span-2">
        <q-file
          v-model="curriculos[slug]"
          class="!bg-white border border-neutral-100/10 !px-10 hover:!bg-neutral-10 label-static ![--input-size:3rem] !max-w-[100%]"
          input-class="relative !whitespace-nowrap "
          clearable
          label="Adicionar arquivo"
          accept=".jpg, .pdf, image/*"
          :rules="[requiredValidation]"
        >
          <template #prepend>
            <div class="flex mx-auto w-full justify-center">
              <q-avatar> <IcoUpload /> </q-avatar>
            </div>
          </template>
        </q-file>
      </UiLabelWrapper>

      <UiLabelWrapper
        v-if="vaga.vaga_generica"
        text="Para qual cargo e nível você gostaria de se candidatar?"
        class="col-span-2"
      >
        <UiInput
          v-model="vagaForm[slug].resposta_vaga_generica"
          :rules="[requiredValidation]"
          autogrow
          placeholder="Ex.: Analista de Dados Pleno"
          class="bg-neutral-10 no-label"
          input-class="!min-h-40  !pt-12"
          size="md"
        >
        </UiInput>
      </UiLabelWrapper>
    </div>
  </q-card>
</template>
