import { createRouter, createWebHistory } from 'vue-router'

// 懒加载页面组件
const Home = () => import('../views/Home.vue')
const History = () => import('../views/History.vue')
const Discipline = () => import('../views/Discipline.vue')
const Messages = () => import('../views/Messages.vue')
const Present = () => import('../views/Present.vue')

const router = createRouter({
  history: createWebHistory(),          // 使用 HTML5 路由
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/history', name: 'History', component: History },
    { path: '/discipline', name: 'Discipline', component: Discipline },
    { path: '/messages', name: 'Messages', component: Messages },
    { path: '/present', name: 'Present', component: Present },
  ],
  scrollBehavior() { return { top: 0 } } // 切页回到顶部
})

export default router
