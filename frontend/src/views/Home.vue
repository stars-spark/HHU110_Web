<script setup>
</script>

<template>
  <!-- 顶部 Hero Banner：铺满视口 -->
  <section class="hero">
    <!-- 版心：随屏幕自适应，宽屏封顶 -->
    <div class="hero-inner">
      <!-- 校徽淡影 -->
      <div class="watermark" aria-hidden="true"></div>

      <!-- 文案区 -->
      <div class="hero-text">
        <h1>青春华章 · 百十河海</h1>
        <p class="subtitle">
          赓续水利底蕴，创新奋进征程 —— 河海大学建校 110 周年专题网站
        </p>

        <div class="buttons">
          <router-link class="btn primary" to="/history">了解校史</router-link>
          <router-link class="btn outline" to="/messages">写下寄语</router-link>
        </div>
      </div>
    </div>

    <!-- 波浪分割线（自适应宽度/高度） -->
    <div class="wave" aria-hidden="true">
      <svg viewBox="0 0 1440 160" preserveAspectRatio="none">
        <path
          fill="url(#grad)"
          d="M0,96 C360,180 1080,0 1440,96 L1440,160 L0,160 Z"
        />
        <defs>
          <linearGradient id="grad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#62a8ff" />
            <stop offset="100%" stop-color="#aee0ff" />
          </linearGradient>
        </defs>
      </svg>
    </div>
  </section>

  <!-- 下方介绍区：同样自适应容器 -->
  <section class="intro">
    <div class="container">
      <h2>百十河海 · 砥砺前行</h2>
      <p>
        河海大学自1915年创办以来，始终秉承“艰苦朴素、实事求是、严格要求、勇于探索”的校训精神，
        在水利、土木、环境、信息等领域培育了大批优秀人才。
      </p>
    </div>
  </section>
</template>

<style scoped>
/* ===== 全局容器：宽屏封顶，窄屏自适应 ===== */
.container,
.hero-inner {
  width: min(1200px, 92vw);   /* 宽屏 ≤1200px；窄屏占 92% 视口宽 */
  margin: 0 auto;
}

/* ===== 顶部 Banner：铺满视口，无黑边 ===== */
.hero {
  position: relative;
  width: 100%;
  min-height: 100vh;      /* 占满可视高度 */
  height: 100svh;         /* 新视口单位，防浏览器UI干扰 */
  display: grid;
  place-items: center;     /* 垂直水平居中内容 */
  overflow: hidden;
  background: linear-gradient(135deg, #e9f3ff 0%, #ffffff 100%);
}

/* 校徽淡影：按短边缩放，避免变形/留边 */
.watermark {
  position: absolute;
  inset: 0;
  margin: auto;
  width: clamp(360px, 35vmin, 520px);  /* 随屏幕缩放 */
  height: clamp(360px, 35vmin, 520px);
  background: url('/hhu-logo.png') no-repeat center/contain;
  opacity: 0.07;
  filter: saturate(0.9);
  pointer-events: none;
}

/* 文案区：自适应内边距，防止贴边 */
.hero-text {
  position: relative;
  text-align: center;
  padding-inline: clamp(12px, 4vw, 48px);
  z-index: 1;
}

/* 标题/副标题：clamp 确保大屏有气势，小屏不溢出 */
.hero-text h1 {
  margin: 0 0 0.5em;
  font-size: clamp(40px, 5vw, 72px);
  font-weight: 800;
  color: #003366;
  letter-spacing: 0.5px;
}
.subtitle {
  margin: 0 auto 2rem;
  max-width: min(900px, 90%);
  font-size: clamp(16px, 1.4vw, 22px);
  color: #1b4b9a;
  line-height: 1.7;
  opacity: 0.9;
}

/* 按钮区：允许换行，避免窄屏拥挤 */
.buttons {
  display: inline-flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

/* 按钮样式 */
.btn {
  display: inline-block;
  font-size: 16px;
  padding: 12px 28px;
  border-radius: 999px;
  font-weight: 700;
  text-decoration: none;
  transition: transform .2s ease, box-shadow .2s ease, background .2s ease, color .2s ease;
}
.primary {
  color: #fff;
  background: linear-gradient(90deg, #1e80ff, #4da3ff);
  box-shadow: 0 6px 12px rgba(30, 128, 255, 0.3);
}
.primary:hover { transform: translateY(-2px); box-shadow: 0 10px 18px rgba(30,128,255,.4); }
.outline {
  color: #1e80ff;
  border: 2px solid #1e80ff;
  background: transparent;
}
.outline:hover { background: #1e80ff; color: #fff; }

/* 波浪：随宽度拉伸，高度自适应 */
.wave {
  position: absolute;
  left: 0; right: 0; bottom: -1px;
  width: 100%;
  line-height: 0;
  pointer-events: none;
}
.wave svg {
  width: 100%;
  height: clamp(100px, 12vh, 160px);
  display: block;
}

/* 介绍区：容器自适应 */
.intro {
  padding: clamp(48px, 8vw, 100px) 0;
  background: #fff;
  text-align: center;
}
.container h2 {
  font-size: clamp(26px, 2.2vw, 36px);
  color: #003366;
  margin: 0 0 12px;
}
.container p {
  font-size: clamp(16px, 1.1vw, 18px);
  color: #335b99;
  line-height: 1.8;
  margin: 0 auto;
  max-width: 900px;
}

/* 超大屏微调（>1600px），让标题更有气势 */
@media (min-width: 1600px) {
  .hero-text h1 { font-size: 80px; }
  .subtitle { font-size: 22px; }
}
</style>
