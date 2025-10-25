<script setup>
import { ref, onMounted } from 'vue'
const list = ref([])
onMounted(async () => {
  const r = await fetch('/api/disciplines')
  list.value = await r.json()
})
</script>

<template>
  <h2>学科特色</h2>
  <div v-for="d in list" :key="d.id">
    <h3>{{ d.name }}</h3>
    <p>{{ d.intro }}</p>
  </div>
</template>
