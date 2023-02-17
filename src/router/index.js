import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ContactPage from '../views/ContactPage.vue'
import AlgorithmPage from '../views/AlgorithmPage.vue'


Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/contact',
    name: 'contact',
    component: ContactPage
  },
  {
    path: '/algorithm',
    name: 'algorithm',
    component: AlgorithmPage
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router