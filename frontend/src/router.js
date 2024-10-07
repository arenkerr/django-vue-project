import { createMemoryHistory, createRouter } from 'vue-router';

import OauthLogin from './components/OauthLogin.vue';
import GitHub from './components/GitHub.vue';

const routes = [
  { path: '/', component: OauthLogin },
  { path: '/github', component: GitHub },
];

export default createRouter({
  history: createMemoryHistory(),
  routes,
});
