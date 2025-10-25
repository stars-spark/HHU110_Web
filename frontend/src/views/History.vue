<script setup>
import { ref, onMounted } from 'vue'
const items = ref([])
onMounted(async () => {
  const r = await fetch('/api/history?page=1&page_size=5') // 用了 Vite 代理就写 /api
  const data = await r.json()
  items.value = data.list || []
})
</script>

<template>
  <h2>校史时间轴</h2>
  <ul>
    <li v-for="i in items" :key="i.id">
      <strong>{{ i.year }}</strong> - {{ i.title }}
    </li>
  </ul>
</template>
