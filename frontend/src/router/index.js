import axios from "axios";
import { createRouter, createWebHashHistory } from "vue-router";
import store from '@/store'
const routes = [
    {
        path: '/',
        redirect: { name: 'Login' },
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/login/login.vue')
    },
    {
        path: '/signup',
        name: 'Signup',
        component: () => import('@/views/signup/signup.vue')
    },
    {
        path: '/home',
        name: 'Home',
        component: () => import('@/views/profile/home.vue')
    },
    {
        path: '/forum',
        name: 'Forum',
        component: () => import('@/views/forum/Page.vue'),
        redirect: '/forum/index',
        children: [
            {
                path: 'dashboard',
                name: 'Dashboard',
                component: () => import('@/views/forum/admin/dashboard.vue')
            },
            {
                path: 'index',
                name: 'Index',
                component: () => import('@/views/forum/index.vue')
            }
        ]
    },
    {
        path: '/admin',
        redirect: '/admin/dashboard',
    },
    // {
    //     path: '/admin/dashboard',
    //     name: 'Dashboard',
    //     component: () => import('@/views/admin/dashboard.vue')
    // },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component: () => import('@/views/404.vue')
    },

]
const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})

router.beforeEach((to, from) => {
    console.log(to, from)
    console.log(router)
    const token = Cookies.get('token')
    // 登陆验证
    if(!token && to.path !== '/login' && to.path !== '/signup') {
        ElNotification({
            title: 'Failure',
            message: '请先登录',
            type: 'error'
          })
        return {name: 'Login'}
    }
    let data = Cookies.get('username')
    store.commit('set_userinfo', {
        username: data,
      })
    // 防止重复登陆
    if (token && to.path === '/login') {
        return { name: 'Forum' }
    }

    return true
})

export default router