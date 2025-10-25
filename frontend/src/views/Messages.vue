<script setup>
import { ref, onMounted } from 'vue'
const content = ref('')
const list = ref([])

async function load() {
  const r = await fetch('/api/messages?page=1&page_size=10')
  const data = await r.json()
  list.value = data.list || []
}
async function send() {
  const txt = content.value.trim()
  if (!txt) return
  await fetch('/api/messages', {
    method: 'POST',
    headers: { 'Content-Type':'application/json' },
    body: JSON.stringify({ content: txt })
  })
  content.value = ''
  await load()
}
async function like(id) {
  await fetch(`/api/messages/${id}/like`, { method: 'POST' })
  await load()
}
onMounted(load)
</script>

<template>
  <h2>青春寄语</h2>
  <div>
    <input v-model="content" placeholder="写点祝福吧…" />
    <button @click="send">发表</button>
  </div>
  <ul>
    <li v-for="m in list" :key="m.id">
      {{ m.content }} （👍 {{ m.likes }}）
      <button @click="like(m.id)">点赞</button>
    </li>
  </ul>
</template>
