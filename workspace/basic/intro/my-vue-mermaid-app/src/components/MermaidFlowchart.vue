<template>
  <div class="card p-3">
    <h5 class="card-title">Mermaid 추리 흐름도</h5>
    <div ref="chartRef" class="mermaid"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import mermaid from 'mermaid'

const chartRef = ref(null)

const flowchartDefinition = `
flowchart TD
A[사건발생] --> B{용의자 수 확인}
B -- 1명 --> C[단서 찾기 시작]
B -- 여러명 --> D[모두 의심하기 시작]
C --> E[왠지 범인은 항상 가까이에...]
D --> E
E --> F[그 순간! 하이바라가 의심 시작]
F --> G[코난:범인은 너야!]
G --> H[코고로 아저씨 기절 -> 명탐정 모드 발동]
H --> I[범인 자백]

style G fill:#fdd,stroke:#f00,stroke-width:2px
`

onMounted(async () => {
  mermaid.initialize({ startOnLoad: false })

  if (!chartRef.value) return

  try {
    const { svg } = await mermaid.render('uniqueFlowchartId', flowchartDefinition)
    chartRef.value.innerHTML = svg
  } catch (e) {
    console.error('Mermaid 렌더링 오류:', e)
  }
})
</script>

<style scoped>
.card {
  max-width: 700px;
  margin: 1rem auto;
}
</style>
