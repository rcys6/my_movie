import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Register from '../views/Register.vue'
import ActivateEmail from '../views/ActivateEmail.vue'
import Login from '../views/Login.vue'
import forgetPassword from '../views/forgetPassword.vue'
import resetPassword from '../views/resetPassword.vue'
import Personal from '../views/Personal.vue'
import changePassword from '../views/changePassword.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },

  {
    path: '/activate/:uid/:token',
    name: 'ActivateEmail',
    component: ActivateEmail
  },

  {
    path: '/Login',
    name: 'Login',
    component: Login
  },

  {
    path: '/reset_password',
    name: 'forgetPassword',
    component: forgetPassword
  },
  
  {
    path: '/password_reset/:uid/:token',
    name: 'resetPassword',
    component: resetPassword
  },
  {
    path: '/personal',
    name: 'Personal',
    component: Personal
  },
  {
    path: '/change_password',
    name: 'changePassword',
    component: changePassword
  },


  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
