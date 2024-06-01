import './assets/main.css';

import { createApp } from 'vue';
import { createVuetify } from 'vuetify';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';
import 'vuetify/styles';
import App from './App.vue';

import { createMemoryHistory, createRouter } from 'vue-router';

import VueCookies from 'vue-cookies';
import { createStore } from 'vuex';
import AuthorizationForm from './components/AuthorizationForm.vue';
import CandidateTable from './components/CandidateTable.vue';
import Main from './components/Main.vue';
import Profile from './components/Profile.vue';
import RegisterForm from './components/RegisterForm.vue';
import ResetPassword from './components/ResetPassword.vue';
import VacanciesTable from './components/VacanciesTable.vue';
import Vacancy from './components/Vacancy.vue';

// vuetify
const vuetify = createVuetify({
  components,
  directives,
})

// router
const routes = [
  { path: '/', component: Main},
  { path: '/register', component: RegisterForm},
  { path: '/auth', component: AuthorizationForm},
  { path: '/candidates', component: CandidateTable },
  { path: '/profile/:id', component: Profile, props: true},
  { path: '/vacancies', component: VacanciesTable },
  { path: '/vacancy/:id', component: Vacancy, props: true},
  { path: '/reset_password', component: ResetPassword },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

// Create a new store instance.
const store = createStore({
  state () {
    return {
      logo_name: "Test",
      logo_url: "./",
      is_auth: false,
      root_url: "http://localhost:8000/",
      user: {
        initials: 'RG',
        fullName: 'Ryan Goosling',
        email: 'ryan.goosling@gmail.com',
      },
    }
  },
  mutations: {
  }
})

createApp(App).use(VueCookies, { expires: '7d'}).use(router).use(vuetify).use(store).mount('#app')