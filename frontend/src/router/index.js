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
import strore from '../store/index.js'
import store from '../store/index.js'

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
    component: Personal ,
    meta:{
      requireLogin:true
    }
  },
  {
    path: '/change_password',
    name: 'changePassword',
    component: changePassword ,
    meta:{
      requireLogin:true
    }
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

const token=localStorage.getItem('token')
if (token) {
  store.commit('setLogiStatus',true)
}

// 路由导航守卫
router.beforeEach((to,from,next)=>{
  if (to.matched.some(record => record.meta.requireLogin) && !strore.state.isLogin) {
    next({name:'Login',query:{jump:to.path}})
  } else {
    next()
  }
})



export default router
