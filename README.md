# 河海大学 110 周年专题站（前后端一体开发）

> 这是一套已经跑通 **前端（Vue + Vite）** 与 **后端（Flask + SQLite）** 的最小可用工程，你只需要按本文档操作，就能开始“设计网页 → 改页面 → 接数据”。

---

## 🗂 目录结构（你可以只记住这几个文件夹）

```

HHU110_Web/
├─ frontend/        # 前端（Vue3 + Vite）：页面、样式、组件、路由都在这里
│  ├─ index.html
│  └─ src/
│     ├─ main.js
│     ├─ App.vue
│     ├─ router/   # 路由配置（把页面“挂到网址路径上”）
│     └─ views/    # 每个页面一个 .vue 文件（首页、校史、寄语等）
├─ backend/         # 后端（Flask）：接口、数据库、业务逻辑都在这里
│  ├─ app.py
│  ├─ models.py     #（可能有）：数据库模型
│  └─ ...
└─ README.md        # 本说明书

````

> 仓库顶层能看到 `frontend/` 和 `backend/` 两个核心目录（其余是编辑器配置）。:contentReference[oaicite:0]{index=0}

---

## 🚀 一分钟快速跑起来

> 要求：安装了 **Node.js 18+** 和 **Python 3.10+**

**1) 拉代码**
```bash
git clone https://github.com/stars-spark/HHU110_Web.git
cd HHU110_Web
````

**2) 启动后端（Flask）**

```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

pip install -r requirements.txt  # 如没有，可先：pip install flask flask-cors sqlalchemy
python app.py
# 看到: Running on http://127.0.0.1:5000
```

**3) 启动前端（Vue + Vite）**

```bash
cd ../frontend
npm i
npm run dev
# 看到: Local: http://localhost:5173/
```

浏览器开 `http://localhost:5173`（前端）
后端接口默认在 `http://127.0.0.1:5000`。

> 如果前端请求后端，建议配置 Vite 代理（见下文 🔗“前后端联通”）。

---

## 🧭 我该从哪里“设计与修改网页”？

你最常改的只有 4 个地方（按改动频率排序）：

1. **`frontend/src/views/`**：每个页面一个 `.vue` 文件（例如 `Home.vue`、`History.vue`、`Messages.vue`）

   * 👉 想新增页面：新建 `views/YourPage.vue`，然后去 `router/index.js` 挂路由（见下节）。

2. **`frontend/src/router/index.js`**：路由表（把“页面文件”挂到“网址路径”）

   ```js
   import { createRouter, createWebHistory } from 'vue-router'
   const Home = () => import('../views/Home.vue')
   const History = () => import('../views/History.vue')

   export default createRouter({
     history: createWebHistory(),
     routes: [
       { path: '/', name: 'Home', component: Home },
       { path: '/history', name: 'History', component: History },
       // 新页面就照这样加
     ]
   })
   ```

3. **`frontend/src/App.vue`**：全站“外壳”（导航栏、页脚、<router-view/> 占位）

   * 👉 想改顶部导航（白字、深蓝透明渐变、吸顶）：改这里的模板/样式即可。

4. **`backend/app.py`**：后端接口（API）

   * 👉 想给页面一个新数据源：在这里加一个 `@app.get('/api/xxx')` 的路由函数，返回 JSON。

---

## 🧩 新手最常做的 4 件事（手把手）

### 1) 新增一个页面（比如“看今朝”）

**(a) 建文件**

```
frontend/src/views/Present.vue
```

```vue
<template>
  <section>
    <h2>看今朝</h2>
    <p>这里放你要展示的内容。</p>
  </section>
</template>
```

**(b) 挂路由**

```
frontend/src/router/index.js
```

```js
{ path: '/present', name: 'Present', component: () => import('../views/Present.vue') }
```

**(c) 导航栏加入口**

```
frontend/src/App.vue
```

```html
<router-link to="/present">看今朝</router-link>
```

刷新页面就能点进新页面。

---

### 2) 修改首页 Banner 的文案/按钮/背景

```
frontend/src/views/Home.vue
```

* 改 `<h1>`、`.subtitle` 文本；
* 按钮的 `to="/某个路由"` 指向你路由中的路径；
* 想用背景图：放一张 `public/banner.jpg`，在样式里将 `.hero-bg` 打开，并换成你的图片路径。

---

### 3) 让页面读后端数据（以“寄语榜单”为例）

**(a) 后端加接口**

```
backend/app.py
```

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许前端跨域访问

@app.get('/api/messages/top')
def top_messages():
    # TODO: 这里用数据库真实查询，这里先返回假数据示例
    data = [
      {"id": 1, "content": "青春河海，加油！", "likes": 20},
      {"id": 2, "content": "载百十年风华，续万千里征程。", "likes": 18},
    ]
    return jsonify(data)
```

**(b) 前端页面调用这个接口**

```
frontend/src/views/TopMessages.vue
```

```vue
<script setup>
import { ref, onMounted } from 'vue'
const tops = ref([])
onMounted(async () => {
  const res = await fetch('/api/messages/top')  // 配了 Vite 代理就能这样写
  tops.value = await res.json()
})
</script>

<template>
  <h2>寄语榜单</h2>
  <ol>
    <li v-for="m in tops" :key="m.id">
      {{ m.content }}（👍{{ m.likes }}）
    </li>
  </ol>
</template>
```

---

### 4) 改主题色、整体风格（蓝白 / 透明深蓝渐变）

* **导航栏配色**：`frontend/src/App.vue` 的 `.navbar` 背景渐变/字体颜色；
* **页面底色**：全局 `frontend/src/style.css`（如 `body { background: #fff; }`）；
* **按钮/标题**：在页面的 `<style scoped>` 中改 `.btn`、`h1/h2` 的颜色/阴影即可。

> 你现在这套样式已支持**PC 端优先**、**全屏 Banner**、**深蓝透明渐变 + 白字**，直接在现有 CSS 上微调即可。

---

## 🔗 前后端联通（Vite 代理，免 CORS 报错）

在 `frontend/vite.config.js/ts` 中添加：

```js
export default {
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000', // Flask
        changeOrigin: true
      }
    }
  }
}
```

这样前端请求可以统一写 `/api/...`，不用写完整后端地址，也不会被浏览器的 CORS 拦截。

---

## 🗃 数据库（SQLite）与模型

* 简单项目推荐用 **SQLite**（一个文件就能保存全部数据）。
* 如果使用 SQLAlchemy，表结构通常在 `backend/models.py`，在 `app.py` 初始化数据库连接：

  ```python
  from sqlalchemy import create_engine
  engine = create_engine('sqlite:///hhu110.db', echo=False)
  ```
* 常用字段：用户（user）、校史（history：year/title）、学科（discipline：name/intro）、寄语（message：content/likes）。

> 你可以先用**假数据**把前端做顺，再把假数据替换成真实数据库查询。

---

## 🧪 本地开发常用命令

```bash
# 后端
cd backend
.venv\Scripts\activate           # Windows
source .venv/bin/activate        # macOS/Linux
python app.py

# 前端
cd frontend
npm run dev
npm run build                    # 打包
npm run preview                  # 本地预览打包结果
```

---

## 🆘 常见问题速查

* **白屏**：打开浏览器 F12 → Console 看红字

  1. `router-link 未识别` → `npm i vue-router@4`，并在 `main.js` 里 `.use(router)`
  2. 找不到挂载点 → `index.html` 有 `<div id="app"></div>` 且 `main.js` 是 `.mount('#app')`
  3. 路由路径大小写不一致 → `Home.vue` ≠ `home.vue`
  4. CSS 把内容“藏了” → 临时注释掉大块样式看是否出现内容
* **CORS 报错**：后端 `CORS(app)` + 前端 Vite 代理 `/api`
* **端口被占用**：改端口或关闭残留进程（`Ctrl + C` 停止 dev）

---

## 📦 部署（最简单思路）

1. **后端**：继续用 Flask（`gunicorn`/`uwsgi` + 反向代理）
2. **前端**：`npm run build` 生成 `frontend/dist/`，用 Nginx/静态托管；将 `/api` 反向代理到 Flask

> 比赛/演示用：也可以直接本地双开（前端 5173，后端 5000），或把前端打包后交给 Flask 静态托管。

---

## 写给使用者

你只要掌握两件事：

1. **页面在 `views/` 新建** → **在 `router/` 挂路径** → **在 `App.vue` 导航里加入口**
2. **需要数据** → **后端 `app.py` 加一个 `/api/xxx`** → **前端用 `fetch('/api/xxx')` 取**

其它的视觉样式（蓝白渐变、白色导航字、按钮样式）都已经替你准备好啦。
慢慢改、边看边学，出问题就看“常见问题速查”，或者来找我.
---

@LJL