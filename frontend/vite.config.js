import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  // GitHub Pages용 base path 설정
  base: process.env.NODE_ENV === 'production' ? '/ai-frontier/' : '/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
  },
  server: {
    port: 3000,
    host: true,
    proxy: {
      // API 요청을 백엔드 서버로 프록시
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      },
      // 웹훅 요청도 프록시
      '/webhook': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
})