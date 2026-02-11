// @ts-check
import withNuxt from '.nuxt/eslint.config.mjs'

export default withNuxt({
  rules: {
    'vue/block-order': [
      'error',
      {
        order: ['script', 'template', 'style'],
      },
    ],
    '@typescript-eslint/no-unused-vars': [
      'off',
      {
        args: 'all',
        argsIgnorePattern: '^_',
        caughtErrors: 'all',
        caughtErrorsIgnorePattern: '^_',
        destructuredArrayIgnorePattern: '^_',
        varsIgnorePattern: '^_',
        ignoreRestSiblings: true,
      },
    ],
    'vue/no-v-html': ['off'],
    'vue/html-self-closing': ['off'],
    'no-unused-vars': [
      'off',
      {
        vars: 'all',
        args: 'after-used',
        caughtErrors: 'all',
        ignoreRestSiblings: false,
      },
    ],
  },
})
