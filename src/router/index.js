import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/explore',
      name: 'explore',
      component: () => import('../views/ExplorerView.vue')
    },
    {
      path: '/users/1',
      name: 'user',
      component: () => import('../views/UserView.vue')
    },
    {
      path: '/cars/new',
      name: 'newcars',
      component: () => import('../views/AddCarView.vue')
    },
    {
      path: '/cars/2',
      name: 'car',
      component: () => import('../views/CarDetailView.vue')
    }
  ]
})

export default router
