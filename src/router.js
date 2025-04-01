import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('./views/HomeView.vue')
  }, 
  {
    path: '/login',
    component: () => import('./views/LoginView.vue')
  },
  {
    path: '/cadastro',
    component: () => import('./views/CadastroView.vue')
  },
  {
    path: '/pesquisa/:livro',
    component: () => import('./views/PesquisaView.vue')
  },
  {
    path: '/paginaLivro/:idLivro',
    component: () => import('./views/LivroPageView.vue')
  },
  {
    path: '/paginaCombo/:idCombo',
    component: () => import('./views/ComboPageView.vue')
  },
  {
    path: '/carrinho',
    component: () => import('./views/CarrinhoView.vue')
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
