<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const progress = ref(0) // 0~1：渐变强度
const clamp = (x, a, b) => Math.min(Math.max(x, a), b)

const onScroll = () => {
  // 滚动 0~240px 之间映射为 0~1，可按需改 240
  progress.value = clamp(window.scrollY / 240, 0, 1)
  // 写入 CSS 变量，供背景透明度/阴影强度使用
  document.documentElement.style.setProperty('--nav-alpha', String(progress.value))
}

onMounted(() => {
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })
})
onBeforeUnmount(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<template>
  <header class="navbar">
    <div class="nav-inner">
      <h1 class="logo">河海大学 110 周年</h1>
      <nav class="nav-links">
        <router-link to="/">首页</router-link>
        <router-link to="/history">校史时间轴</router-link>
        <router-link to="/discipline">学科特色</router-link>
        <router-link to="/messages">青春寄语</router-link>
        <router-link to="/present">看今朝</router-link>
      </nav>
    </div>
  </header>

  <main class="main-content">
    <router-view />
  </main>
</template>

<style scoped>
/* 置顶时不显示任何边线；滚动后再逐步显现 */
:global(:root){
  --nav-alpha: 0;           /* 0~1 由脚本写入 */
  --nav-blue: 0,45,128;     /* 深蓝基色 #002D80 -> rgb */
}

.navbar{
  position: fixed; top:0; left:0; right:0; z-index:1000;
  width: 100%;

  /* 顶部深蓝 → 透明；透明度由 --nav-alpha 渐进增强 */
  background:
    linear-gradient(
      to bottom,
      rgba(var(--nav-blue), calc(.90 * var(--nav-alpha))) 0%,
      rgba(var(--nav-blue), calc(.70 * var(--nav-alpha))) 40%,
      rgba(var(--nav-blue), calc(.00 * var(--nav-alpha))) 100%
    );

  /* 置顶时无边线；滚动越多越明显（利用 alpha 渐变） */
  border-bottom: 1px solid rgba(255,255,255, calc(.20 * var(--nav-alpha)));
  box-shadow: 0 6px 18px rgba(0,0,0, calc(.12 * var(--nav-alpha)));
  transition: background .18s linear, border-color .18s linear, box-shadow .18s linear;
  -webkit-font-smoothing: antialiased;
}

.nav-inner{
  max-width: 1280px; margin: 0 auto;
  padding: 16px 40px;
  display:flex; align-items:center; justify-content:space-between;
}

.logo{ color:#fff; font-weight:700; font-size:1.25rem; letter-spacing:1px; margin:0; }
.nav-links{ display:flex; gap:36px; }
.nav-links a{
  color:#fff; text-decoration:none; font-weight:600; padding-bottom:4px; position:relative;
  transition: color .2s ease;
}
.nav-links a:hover{ color:#aee0ff; }
.nav-links a::after{
  content:""; position:absolute; left:0; bottom:0; height:2px; width:0%;
  background: currentColor; transition: width .2s ease;
}
.nav-links a:hover::after{ width:100%; }
.nav-links a.router-link-active{ color:#aee0ff; }
.nav-links a.router-link-active::after{ width:100%; }

.main-content{
  /* 根据你导航高度调这个值，或用前面那种 JS 计算 var(--nav-h) 方案 */
  margin-top: 80px;
  padding: 48px 6vw;
}

/* ---- Home.vue 波浪“发蓝细边”修复建议 ---- */
/* 在你的 Home.vue 里给 .wave / svg 增强抗锯齿与轻微下移 */
:global(.wave){ bottom: -2px !important; transform: translateZ(0); }
:global(.wave svg){ shape-rendering: geometricPrecision; transform: translateZ(0); }
</style>
