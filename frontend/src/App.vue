<script setup>
import { ref, onMounted } from 'vue'
const ping = ref('')
const messages = ref([])

onMounted(async () => {
  ping.value = (await (await fetch('http://127.0.0.1:5000/api/ping')).json()).msg
  const r = await fetch('http://127.0.0.1:5000/api/messages?page=1&page_size=5')
  messages.value = (await r.json()).list
})
</script>

<template>
  <h1>青春华章 · 百十河海</h1>
  <p>后端连通：{{ ping }}</p>
  <h2>最新寄语</h2>
  <ul>
    <li v-for="m in messages" :key="m.id">
      {{ m.user }}：{{ m.content }}（👍 {{ m.likes }}）
    </li>
  </ul>
</template>
