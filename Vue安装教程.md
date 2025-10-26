
> 适用于 Windows 10/11（macOS、Linux 也几乎一样）
> 推荐使用 **Vue 3 + Vite**（最新版模板，启动更快）

---

## 🧩 一、认识 Vue

**Vue.js** 是一个前端框架，用来写网页页面和交互逻辑。
它让我们可以把网页拆成一个个“组件”，像搭积木一样设计网站。
而我们要用到的版本是：

> **Vue 3 + Vite**：官方推荐的现代版 Vue 工程结构。
> 优点：启动快、代码热更新、结构清晰。

---

## ⚙️ 二、安装前准备

在安装 Vue 前，你需要准备好两个基础环境：

| 工具      | 作用                             | 下载地址                                                             |
| ------- | ------------------------------ | ---------------------------------------------------------------- |
| Node.js | 运行 JavaScript 环境 + 附带 npm 包管理器 | [https://nodejs.org/](https://nodejs.org/)                       |
| VS Code | 写代码的编辑器（推荐）                    | [https://code.visualstudio.com/](https://code.visualstudio.com/) |

---

### 🪄 1. 安装 Node.js

1. 打开 [Node.js 官网](https://nodejs.org/zh-cn)。
2. 点击左边的 **LTS（长期支持版）** 按钮。
3. 下载后一路“下一步”安装即可。

安装完后打开命令行（Win + R → 输入 `cmd`）：

```bash
node -v
npm -v
```

如果能输出版本号，例如：

```
v18.19.1
9.6.7
```

说明安装成功 ✅

---

### 🪄 2. （可选）安装 Git

如果你要从 GitHub 下载项目（比如我们的 `HHU110_Web`），建议安装 Git。

👉 [https://git-scm.com/downloads](https://git-scm.com/downloads)

装完后命令行输入：

```bash
git --version
```

看到版本号即成功。

---

### 🪄 3. 安装 VS Code 编辑器

👉 [https://code.visualstudio.com/](https://code.visualstudio.com/)

打开后安装两个插件：

* ✅ **Volar**（Vue 官方语法高亮和提示）
* ✅ **ESLint**（自动检查代码格式）

---

## 🚀 三、创建第一个 Vue 项目

Vue 项目推荐用官方工具 **Vite** 来创建。

### 🧱 步骤 1：进入想放项目的文件夹

```bash
cd D:\projects   # 自己的任意目录
```

### 🧱 步骤 2：创建项目

运行命令：

```bash
npm create vite@latest my-vue-app
```

Vite 会问你几个问题：

```
✔ Project name: … my-vue-app
✔ Select a framework: › Vue
✔ Select a variant: › JavaScript
```

> 如果它问你 “Use rolldown-vite (Experimental)?” 选 **No** 就行。

---

### 🧱 步骤 3：进入项目文件夹并安装依赖

```bash
cd my-vue-app
npm install
```

---

### 🧱 步骤 4：启动项目

```bash
npm run dev
```

看到输出：

```
VITE v5.x.x  ready in 400 ms
➜  Local:   http://localhost:5173/
```

浏览器打开 [http://localhost:5173](http://localhost:5173)
✨ 页面显示 Vue 的 Logo 和一些按钮，就成功啦！

---

## 🪄 四、项目结构介绍（你只需记住这些）

```
my-vue-app/
├─ index.html               # 网页入口
├─ package.json             # 项目配置文件
└─ src/
   ├─ main.js               # Vue 启动文件（入口）
   ├─ App.vue               # 根组件（整个网页外壳）
   ├─ assets/               # 图片资源
   └─ components/           # 小组件（按钮、卡片等）
```

---

## 🎨 五、如何修改网页内容

打开 `src/App.vue`：
你会看到：

```vue
<template>
  <h1>Hello Vue!</h1>
</template>
```

改成：

```vue
<template>
  <h1>你好，这是我们的第一个网页 ❤️</h1>
</template>
```

保存后浏览器会**自动刷新**，看到新文字说明修改成功。

---

## 🧭 六、增加路由（多页面导航）

安装 Vue Router：

```bash
npm i vue-router@4
```

在 `src/` 新建一个文件夹 `router/`，里面创建 `index.js`：

```js
import { createRouter, createWebHistory } from 'vue-router'

const Home = () => import('../views/Home.vue')
const About = () => import('../views/About.vue')

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
  ],
})
```

在 `src/main.js` 里：

```js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
```

然后在 `App.vue` 里加：

```vue
<template>
  <nav>
    <router-link to="/">首页</router-link>
    <router-link to="/about">关于</router-link>
  </nav>
  <router-view/>
</template>
```

保存后即可在两个页面之间切换。

---

## 🖌 七、安装 UI 样式框架（可选）

你可以用现成的样式库来快速美化：

| 名称           | 安装命令                                                                   | 特点        |
| ------------ | ---------------------------------------------------------------------- | --------- |
| Element Plus | `npm i element-plus`                                                   | 官方推荐，风格现代 |
| TailwindCSS  | `npm i -D tailwindcss postcss autoprefixer && npx tailwindcss init -p` | 轻量可自定义    |
| Bootstrap    | `npm i bootstrap`                                                      | 经典简约风     |

---

## 💡 八、打包与部署

当你写好网页后，运行：

```bash
npm run build
```

在项目目录会生成 `dist/` 文件夹，它就是可以直接上传的静态网页。

---

## 🧰 九、常见问题

| 问题                   | 原因与解决                                                          |
| -------------------- | -------------------------------------------------------------- |
| 页面空白                 | 看控制台红字，常见是路径写错或组件名大小写不对                                        |
| 报错 “router-link 未定义” | 你没在 `main.js` 里 `.use(router)`                                 |
| npm 安装超慢             | 用淘宝镜像：`npm config set registry https://registry.npmmirror.com` |
| 想重置项目                | 删除 `node_modules` 和 `package-lock.json`，再 `npm i`              |

