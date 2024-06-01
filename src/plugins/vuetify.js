// import this after install `@mdi/font` package
import '@mdi/font/css/materialdesignicons.css'

import { createVuetify } from 'vuetify'
import 'vuetify/iconsets'
import 'vuetify/styles'

// const myCustomLightTheme = {
//   dark: false,
//   colors: {
//     background: '#FFFFFF',
//     surface: '#FFFFFF',
//     'surface-bright': '#FFFFFF',
//     'surface-light': '#EEEEEE',
//     'surface-variant': '#424242',
//     'on-surface-variant': '#EEEEEE',
//     primary: '#fdfbff',
//     secondary: '#dce2fa',
//     'secondary-darken-1': '#018786',
//     error: '#B00020',
//     info: '#2196F3',
//     success: '#4CAF50',
//     warning: '#FB8C00',
//   },
// }

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    iconfont: 'mdi'
  })
  app.vueApp.use(vuetify)
})
