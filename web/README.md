# web — frontend React (stack React + FastAPI)

Frontend de práctica en **React 18 + TypeScript + Vite** con un botón **"Probar backend"** que llama a `GET api/ping` del backend hermano
`../micro` (FastAPI). Todo el contenido es ficticio y educativo.

## Stack

| Pieza | Detalle |
|---|---|
| UI | React 18, TypeScript 5 |
| Empaquetado | Vite **4.5** (la última línea que soporta Node 16), `@vitejs/plugin-react` |
| HTTP | `axios` 1.7.9 |
| Calidad | ESLint 8 con `@typescript-eslint` 6 |
| Herramientas | Node 16.16 y **yarn** |
| Puerto | **3003** (`strictPort`: si está ocupado, falla en vez de cambiar de puerto) |

## Cómo correrlo

```powershell
cd web
yarn install
yarn dev            # http://localhost:3003
yarn build          # tsc && vite build -> dist/
yarn lint           # ESLint con --max-warnings 0
```

El backend debe estar encendido en el 8083 (`../micro`).

## Configuración

`.env` → `VITE_URL_API=http://localhost:8083/api/`. Solo lleva una URL pública, por eso se versiona. En el código se lee con `import.meta.env.VITE_URL_API`
y se usa **en un solo lugar** (`src/services/api.ts`).

## Estructura (`src/`)

| Archivo | Responsabilidad |
|---|---|
| `App.tsx` | Pantalla: botón, estado de carga y resultado |
| `services/api.ts` | Instancia de `axios` con la URL base |
| `services/pingService.ts` | Llamada `GET ping` tipada |
| `types/respuesta.ts` | Interfaz `Respuesta` (`RESPUESTA`, `ESTADO`, `BASEDEDATOS?`) |
| `main.tsx`, `index.css` | Arranque y estilos |

Si el backend falla, se muestra un mensaje genérico: no se exponen detalles técnicos al usuario.

## Trampas ya resueltas (no repetir)

- `package.json` lleva `resolutions.node-releases = 2.0.44` (Node 16.16 falla con la versión más nueva). Usa **yarn**: `npm` ignora `resolutions`.
- El proyecto se generó con `create-vite@4.4.1` (las versiones recientes piden Node 18). No subas Vite sin subir Node.
- Con `Invoke-WebRequest` de PowerShell, Vite responde 404 en `/` porque no envía `Accept: text/html`; con un navegador o `curl` responde bien.

## Estado de verificación (2026-09-25)

`yarn build` ✔ · `yarn lint` ✔ (sin advertencias) · clic real en Chrome contra el backend FastAPI: `pong (SQLite …)` sin errores de consola ✔.
**No tiene pruebas automáticas** (ni Vitest ni Testing Library todavía).
