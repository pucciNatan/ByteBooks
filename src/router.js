import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    component: () => import('./views/HomeView.vue')
  }, {
    path: '/sobre',
    component: () => import('./views/SobreView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
