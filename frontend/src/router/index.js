import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'
import AppointmentsView from '../views/AppointmentsView.vue'
import UsersView from '../views/UsersView.vue'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: DashboardView
  },
  {
    path: '/appointments',
    name: 'appointments',
    component: AppointmentsView
  },
  {
    path: '/users',
    name: 'users',
    component: UsersView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router