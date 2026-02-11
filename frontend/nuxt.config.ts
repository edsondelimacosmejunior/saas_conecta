// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  future: {
    compatibilityVersion: 4,
  },

  runtimeConfig: {
    // server-only
    apiSecret: process.env.API_SECRET,
    apiUrl: process.env.API_URL,

    public: {
      // No Replit o host muda; deixe configurável por env
      appUrl: process.env.NUXT_PUBLIC_APP_URL || '',
      // Use sempre /api no browser e deixe o Nuxt proxiar pro Django
      apiBase: process.env.NUXT_PUBLIC_API_BASE || '/api',
    },
  },

  imports: {
    dirs: ['services', 'stores'],
  },

  app: {
    pageTransition: { name: 'page', mode: 'default' },
  },

  routeRules: {
    '/*': { ssr: false },
    '/vagas/**': { ssr: false },
    '/vagas/*/form': { ssr: false },
  },

  modules: [
    'nuxt-quasar-ui',
    '@nuxt/eslint',
    'nuxt-svgo',
    '@nuxt/fonts',
    '@pinia/nuxt',
    'pinia-plugin-persistedstate/nuxt',
    'nuxt-gtag',
  ],

  gtag: {
    id: 'G-M4HNKVZSE2',
  },

  $production: {
    scripts: {
      registry: {
        hotjar: {
          id: 5269880, // your id
        },
      },
    },
  },

  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  eslint: {
    config: {
      autoInit: true,
    },
  },

  svgo: {
    global: false,
    componentPrefix: 'ico',
    defaultImport: 'component',
  },

  quasar: {
    lang: 'pt-BR',
    plugins: ['Dialog', 'Notify'],
  },

  // ⚡ Vite
  vite: {
    assetsInclude: ['**/*.lottie'],

    resolve: {
      alias: {
        ['quasar/dist/quasar.sass']: './empty.css',
        ['quasar/dist/quasar.css']: './empty.css',
      },
    },

    css: {
      preprocessorOptions: {
        sass: {
          api: 'modern-compiler',
        },
      },
    },

    // Replit: expor o dev server externamente na porta pública
    server: {
      host: true,
      port: Number(process.env.PORT) || 3000,
      strictPort: true,
    },
  },

  compatibilityDate: '2025-01-06',
  devtools: { enabled: true },

  nitro: {
    // No Replit, evite preset de deploy (netlify-edge). Em produção você pode reativar.
    // preset: 'netlify-edge',

    // Replit: proxy /api -> Django interno
    devProxy: {
      '/api': {
        target: process.env.API_PROXY_TARGET || 'http://127.0.0.1:8000/api',
        changeOrigin: true,
      },
    },

    routeRules: {
      '/api/**': { swr: true },
    },
  },
})
