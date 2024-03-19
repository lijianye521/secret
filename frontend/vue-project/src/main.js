// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// 导入 Bootstrap 和 BootstrapVue CSS 文件（顺序很重要）
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
const app = createApp(App)

app.use(router)


app.mount('#app')
