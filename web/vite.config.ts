import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Puerto propio (3003): no choca con Nuxt (3001) ni con el proyecto real (3000).
export default defineConfig({
  plugins: [react()],
  server: { port: 3003, strictPort: true },
})
