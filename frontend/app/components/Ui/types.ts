import type { QBtnProps, QSelect } from 'quasar'

export interface UiButtonProps extends QBtnProps {
  /** Define o tamanho personalizado do botão. */
  size: 'md' | 'sm' | 'lg'
  /** Define a cor personalizado do botão. */
  tipo: 'primary' | 'secondary' | 'tertiary'
  iconSize: string
  // eslint-disable-next-line @typescript-eslint/no-unused-expressions
}
;[]

export interface UiSelectProps extends QSelect {}
