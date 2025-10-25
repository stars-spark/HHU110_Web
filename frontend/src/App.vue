<script setup>
// 这里暂时不需要写脚本逻辑
</script>

<template>
  <!-- 导航栏 -->
  <header class="navbar">
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/history">校史时间轴</router-link>
      <router-link to="/discipline">学科特色</router-link>
      <router-link to="/messages">青春寄语</router-link>
      <router-link to="/present">看今朝</router-link>
    </nav>
  </header>

  <!-- 页面内容 -->
  <main class="main-content">
    <router-view /> <!-- 不同页面会显示在这里 -->
  </main>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to right, #6ea8fe, #a6e1fa);
  padding: 12px;
  border-bottom: 1px solid #ddd;
}
.navbar nav {
  display: flex;
  gap: 20px;
}
.navbar a {
  text-decoration: none;
  color: #003366;
  font-weight: bold;
  transition: 0.2s;
}
.navbar a.router-link-active {
  color: #0077ff;
  border-bottom: 2px solid #0077ff;
}
.main-content {
  padding: 24px;
}
</style>
