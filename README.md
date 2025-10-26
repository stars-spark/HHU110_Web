# HHU110_Web · 前后端分离网站

> 这是一个**前端（Vue）+ 后端（Python）**的前后端分离项目。这份说明从零开始带你把站点跑起来、改样式、加页面、连后端。

## 目录结构

仓库根目录大致如下（以你当前仓库为准）：

```
.
├─ frontend/   # 前端工程（Vue）
├─ backend/    # 后端工程（Python API）
├─ .vscode/    # 可选：VS Code 配置
└─ README.md
```

> 仓库语言占比：Vue/JS/CSS/HTML + Python（见 GitHub 语言统计）。([GitHub][1])

---

## 快速开始（5 分钟跑起来）

### 1) 克隆代码

```bash
git clone https://github.com/stars-spark/HHU110_Web.git
cd HHU110_Web
```

### 2) 启动前端（Vue）

> 需要 Node.js（建议 LTS 版本 18/20）。不会安装的话去 nodejs.org 下载“LTS”。

```bash
cd frontend
# 任意包管理器三选一（会哪个用哪个）：
npm install        # 或 pnpm install / yarn
npm run dev        # 启动开发服务器（看到本地地址就成功了）
```

打开终端里显示的本地地址（通常是 `http://localhost:5173` 或 `http://localhost:3000`）。

### 3) 启动后端（Python）

> 需要 Python 3.10+（建议）。如果你没环境，先装 Python，再回到下面操作。

```bash
cd ../backend
# 创建并激活虚拟环境（Windows）
python -m venv .venv
. .venv/Scripts/activate

# 安装依赖（若仓库里有 requirements.txt 就执行这行）
pip install -r requirements.txt

# 启动后端（按你项目实际命令，常见示例）：
# 若是 FastAPI：
uvicorn main:app --reload --port 8000
# 若是 Flask：
# python app.py
```

后端启动成功后，记住它的访问地址（例如 `http://localhost:8000`）。

---

## 前后端“连上网”：跨域与接口地址

1. **前端配置后端地址**
   在 `frontend` 里常见会有：

   * `.env.development` / `.env`（形如 `VITE_API_BASE=http://localhost:8000`），或
   * 某个 `src/services/api.ts|js` 里写了 `baseURL`。
     把它改成你的后端地址，比如：

   ```env
   VITE_API_BASE=http://localhost:8000
   ```

2. **后端允许跨域（CORS）**

   * FastAPI 示例：

     ```python
     from fastapi import FastAPI
     from fastapi.middleware.cors import CORSMiddleware

     app = FastAPI()
     app.add_middleware(
         CORSMiddleware,
         allow_origins=["http://localhost:5173", "http://localhost:3000"],
         allow_credentials=True,
         allow_methods=["*"],
         allow_headers=["*"],
     )
     ```
   * Flask 可用 `flask-cors`：

     ```bash
     pip install flask-cors
     ```

     ```python
     from flask import Flask
     from flask_cors import CORS

     app = Flask(__name__)
     CORS(app, resources={r"/*": {"origins": "*"}})
     ```

---

## 我只改前端页面，怎么下手？

> **目标**：能改文案、颜色、加板块

### A. 找页面文件

* 通常入口在 `frontend/src/App.vue` 和 `frontend/src/main.ts|js`。
* 具体页面在 `frontend/src/pages` 或 `frontend/src/views`。
* 公共组件在 `frontend/src/components`。

### B. 改文案与样式

* 文案：直接改对应 `.vue` 文件里的模板区 `<template>`。
* 颜色/布局：改 `.vue` 的 `<style>` 部分，或全局样式（如 `src/assets/` 下的 css）。

### C. 新增一个页面（以 Vite + Vue Router 为例）

1. 创建文件 `frontend/src/pages/About.vue`：

   ```vue
   <template>
     <section class="container">
       <h1>关于我们</h1>
       <p>这里写你的内容～</p>
     </section>
   </template>

   <script setup>
   ```

// 如果需要逻辑，这里写 </script>

   <style scoped>
   .container { max-width: 900px; margin: 40px auto; line-height: 1.8; }
   </style>

````
2. 在路由里加一条（通常是 `frontend/src/router/index.ts|js`）：
```ts
{ path: '/about', name: 'About', component: () => import('../pages/About.vue') }
````

3. 在导航处加链接（如 `Navbar.vue`）：

   ```html
   <router-link to="/about">关于</router-link>
   ```

刷新前端地址就能看到新页面了。

---

## 我想从前端调用后端接口，怎么写？

**最小示例（使用 fetch）：**

```ts
const base = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000';

async function getMessages() {
  const res = await fetch(`${base}/api/messages`);
  if (!res.ok) throw new Error('网络错误');
  return await res.json();
}

getMessages().then(data => {
  console.log('后端返回：', data);
});
```

> 如果项目用的是 `axios`，把 `fetch` 换成 `axios.get(...)` 即可。

---

## 我不会后端，但想做“能存数据”的功能？

（FastAPI + SQLite）：

1. 安装依赖

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic
   ```

2. 在 `backend` 新建 `main.py`（最小可用）：

   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   from pydantic import BaseModel

   app = FastAPI()
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

   class Message(BaseModel):
       author: str
       content: str

   DB: list[Message] = []

   @app.get("/api/messages")
   def list_messages():
       return DB

   @app.post("/api/messages")
   def add_message(msg: Message):
       DB.append(msg)
       return {"ok": True}
   ```

3. 启动：

   ```bash
   uvicorn main:app --reload --port 8000
   ```

4. 前端就能 `GET /api/messages` / `POST /api/messages` 了，后面你可以再把 `list` 换成 SQLite（持久化）。

---

## 常见问题

* **前端装依赖报错**
  尝试把 Node 升级到 LTS；或者删除 `node_modules` + `package-lock.json` 再安装：

  ```bash
  rm -rf node_modules package-lock.json
  npm install
  ```

* **前端白屏**
  打开浏览器控制台（F12）看错误；多数是路由路径或组件导入路径写错了。

* **后端端口被占用**
  把端口改成别的（如 8001）：`uvicorn main:app --reload --port 8001`，同时把前端的 `VITE_API_BASE` 改一致。

* **跨域错误（CORS）**
  按上面“跨域与接口地址”章节加中间件，或确认前端 `VITE_API_BASE` 指向后端的真实地址。

---

## 打包与部署（最简单路径）

### 前端打包

```bash
cd frontend
npm run build
# 产物通常在 dist/ 目录
```

* **纯静态部署**：把 `dist/` 上传到任意静态空间（GitHub Pages、Netlify、Vercel、Nginx 静态目录都行）。

### 后端部署

* **教学/演示用**：本地跑 `uvicorn` 就够。
* **线上轻量**：用 `uvicorn + nginx` 或者丢到 Render/Zeabur/阿里云轻量，端口映射出来即可。

---

## 开发建议

* 组件化：把页面拆成多个小组件（`src/components/`），可复用、好维护。
* 设计系统：提前想好**配色、间距、字号**，写在 `:root{ --primary: ... }` 或 `tailwind.config`，做统一风格。
* 状态管理：数据复杂时考虑 Pinia（很简单好用）。
* 路由组织：一级页放 `pages/`，页面内块放 `components/`；命名清晰，后续维护不迷路。
* 提交规范：一次改一个点，写清晰提交信息（如 `feat: add About page` / `fix: header overflow`）。

---

## 项目维护者

* Repo: `stars-spark/HHU110_Web`（主分支：`main`）([GitHub][1])



