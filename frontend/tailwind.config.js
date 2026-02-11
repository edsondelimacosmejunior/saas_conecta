import typography from './app/utils/typography'
const plugin = require('tailwindcss/plugin')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/components/**/*.{js,vue,ts}',
    './app/components/*.{js,vue,ts}',
    './app/layouts/**/*.vue',
    './app/pages/**/*.vue',
    './app/pages/*.vue',
    './app/utils/**/*.{js,ts}',
    './app/plugins/**/*.{js,ts}',
    './app/app.vue',
  ],
  theme: {
    colors: {
      white: withOpacity('--white'),
      transparent: 'rgba(255, 255, 255, 0)',
      'neutral-100': withOpacity('--neutral-100'),
      'neutral-70': withOpacity('--neutral-70'),
      'neutral-60': withOpacity('--neutral-60'),
      'neutral-30': withOpacity('--neutral-30'),
      'neutral-20': withOpacity('--neutral-20'),
      'neutral-10': withOpacity('--neutral-10'),

      'primary-light': withOpacity('--primary-light'),
      'primary-pure': withOpacity('--primary-pure'),
      'primary-pure-10': withOpacity('--primary-pure-10'),
      'primary-pure-dark': withOpacity('--primary-pure-dark'),

      'alert-error-10': withOpacity('--alert-error-10'),
      'alert-error': withOpacity('--alert-error'),

      'alert-warning-10': withOpacity('--alert-warning-10'),
      'alert-warning': withOpacity('--alert-warning'),

      'alert-success-10': withOpacity('--alert-success-10'),
      'alert-success': withOpacity('--alert-success'),
    },
    extend: {},
    spacing: {
      0: '0',
      1: '1px',
      2: '0.125rem',
      3: '3px',
      4: '0.25rem',
      6: ' 0.38rem',
      8: '0.5rem',
      9: '0.56rem',
      10: '.625rem',
      12: '0.75rem',
      14: '0.875rem',
      16: '1rem',
      18: '1.13rem',
      20: '1.25rem',
      24: '1.5rem',
      28: '1.75rem',
      32: '2rem',
      34: '2.75rem',
      40: '2.5rem',
      42: '2.63rem',
      48: '3rem',
      56: '3.5rem',
      64: '4rem',
      72: '4.5rem',
      80: '5rem',
      96: '6rem',
      120: '7.5rem',
      160: '10rem',
    },
  },
  plugins: [
    plugin(function ({ addUtilities }) {
      // prettier-ignore
      addUtilities(typography)
    }),
  ],
}

function withOpacity(variableName) {
  return ({ opacityValue }) => {
    if (opacityValue !== undefined) {
      return `rgba(var(${variableName}), ${opacityValue})`
    }
    return `rgb(var(${variableName}))`
  }
}
