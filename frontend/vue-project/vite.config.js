import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  proxy: {
    // 配置代理规则
    '/api': {
      target: 'http://localhost:8000', // 后台服务所在的源
      changeOrigin: true, // 需要虚拟托管站点，以便可以跨域
      rewrite: (path) => path.replace(/^\/api/, '') // 重写路径，去除/api
    }
  }

})
