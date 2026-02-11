<script setup>
import { useDialogPluginComponent } from 'quasar'

const props = defineProps({
  vaga: { type: Object, default: () => ({}) },
})

/** @type {import('../../services/d.types').Vaga} */
const vaga = props.vaga

defineEmits([...useDialogPluginComponent.emits])

const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()
</script>

<template>
  <q-dialog ref="dialogRef" @hide="onDialogHide">
    <q-card
      class="!p-24 !rounded-[1rem] w-full max-w-[800px] h-full !flex flex-col flex-nowrap"
    >
      <header class="flex items-center gap-16 mb-16 -mt-8 !flex-nowrap">
        <IcoTitle class="size-32 transparent shrink-0" />
        <h1 class="text-title-3 text-neutral-100">
          {{ vaga.titulo }}
        </h1>
        <UiButton
          class="!size-48 !p-0 justify-center items-center ml-auto self-start shrink-0"
          rounded
          @click="onDialogCancel"
        >
          <q-icon class="text-neutral-60" size="24px" name="close"></q-icon
        ></UiButton>
      </header>
      <Suspense>
        <VagaAttributes
          v-if="!isMobile()"
          :vaga
          class="!shadow-none !border !border-neutral-100/10 mb-16"
        />
        <template #fallback>
          <UiLoader />
        </template>
      </Suspense>
      <q-scroll-area class="h-full overflow-x-hidden">
        <Suspense>
          <VagaAttributes
            v-if="isMobile()"
            :vaga
            class="!shadow-none !border !border-neutral-100/10 mb-16"
          />
          <template #fallback>
            <UiLoader />
          </template>
        </Suspense>
        <Suspense>
          <VagaDescription
            :vaga
            class="mt-12 mb-64 flex flex-col !shadow-none !border-none !p-0 !px-8 !pt-8"
          >
            <VagaResponsabilities :vaga />
            <VagaDifferentials :vaga />
          </VagaDescription>
          <template #fallback>
            <UiLoader />
          </template>
        </Suspense>
      </q-scroll-area>
    </q-card>
  </q-dialog>
</template>
