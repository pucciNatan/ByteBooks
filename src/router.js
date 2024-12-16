import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('./views/HomeView.vue')
  }, {
    path: '/login',
    component: () => import('./views/CadastroLoginView.vue')
  },
  {
    path: '/pesquisa/:livro',
    component: () => import('./views/PesquisaView.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
