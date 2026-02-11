<script setup>
import { useDialogPluginComponent } from 'quasar'

defineEmits([...useDialogPluginComponent.emits])

const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()
</script>

<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide">
    <q-card
      class="!p-24 !rounded-[1rem] w-full max-w-[800px] h-full !flex flex-col flex-nowrap"
    >
      <header class="flex items-center gap-16 mb-16 -mt-8">
        <h1 class="text-title-3 text-neutral-100 max-lg:pr-32">Termos de Uso da Ferramenta Conecta Novadata</h1>
        <UiButton
          class="!size-48 !p-0 justify-center items-center ml-auto max-lg:!absolute max-lg:top-8 max-lg:right-8 !shadow-none  shrink-0"
          rounded
          @click="onDialogCancel"
        >
          <q-icon class="text-neutral-60" size="24px" name="close"></q-icon
        ></UiButton>
      </header>

      <q-scroll-area class="h-full">
        <div class="flex flex-col gap-32 text-neutral-100 text-paragraph-2 mt-24 mb-32 pr-48 max-lg:pr-8 max-lg:mt-8">

          <p>
            <strong> 1. Introdução</strong> A ferramenta Conecta Novadata tem
            como objetivo agrupar informações sobre candidatos para facilitar a
            análise de oportunidades de trabalho na área de tecnologia. A
            transparência e a proteção dos dados pessoais são prioridades da
            Novadata, em conformidade com a Lei Geral de Proteção de Dados (LGPD
            - Lei nº 13.709/2018).<br />
          </p>
          <p>
            <strong>2. Coleta e Uso das Informações</strong> Os dados pessoais
            fornecidos pelos candidatos, incluindo informações como nome,
            e-mail, telefone, experiência profissional e qualificações, serão
            utilizados exclusivamente para sugerir sua contratação e respectiva
            alocação em projetos de desenvolvimento nos quais a Novadata preste
            serviço. O uso dessas informações ocorrerá sempre mediante
            consentimento explícito do candidato.<br />
          </p>
          <p>
            <strong>3. Compartilhamento de Informações</strong> Os dados dos
            candidatos poderão ser compartilhados com empresas contratantes e
            clientes da Novadata exclusivamente para fins de recrutamento e
            seleção. A Novadata não comercializa, vende ou compartilha os dados
            para qualquer outro propósito, garantindo que terceiros envolvidos
            no processo de seleção estejam alinhados com as diretrizes da
            LGPD.<br />
          </p>
          <p>
            <strong>4. Armazenamento e Proteção dos Dados</strong> A Novadata
            adota medidas técnicas e organizacionais para proteger os dados
            pessoais contra acessos não autorizados, perda, alteração ou
            divulgação indevida. Os dados serão armazenados em ambiente seguro e
            poderão ser mantidos pelo tempo necessário para o propósito de
            recrutamento, respeitando os prazos legais aplicáveis.<br />
          </p>
          <p>
            <strong>5. Direitos dos Titulares de Dados</strong> Os candidatos
            têm direito a acessar, corrigir, atualizar e excluir seus dados
            pessoais. Além disso, podem solicitar a revogação do consentimento e
            a portabilidade dos seus dados. Para exercer esses direitos, basta
            entrar em contato com a Novadata através dos canais oficiais de
            atendimento.<br />
          </p>
          <p>
            <strong>6. Consentimento do Candidato</strong> Ao preencher os dados
            na ferramenta Conecta Novadata, o candidato manifesta seu
            consentimento livre, informado e inequívoco para o tratamento de
            seus dados pessoais nos termos estabelecidos neste documento. O
            consentimento poderá ser revogado a qualquer momento mediante
            solicitação expressa.<br />
          </p>
          <p>
            <strong>7. Alterações nos Termos de Uso</strong> A Novadata se
            reserva o direito de modificar estes Termos de Uso conforme
            necessário para atender a requisitos legais, regulamentares ou
            operacionais. Alterações significativas serão informadas previamente
            aos candidatos, garantindo total transparência.<br />
          </p>
          <p>
            <strong> 8. Contato e Dúvidas</strong> Para quaisquer dúvidas,
            solicitações ou esclarecimentos sobre a política de privacidade e
            proteção de dados, os candidatos podem entrar em contato com a
            Novadata através dos canais de comunicação disponíveis em nosso site
            oficial.<br />
          </p>
        </div>
      </q-scroll-area>
    </q-card>
  </q-dialog>
</template>
